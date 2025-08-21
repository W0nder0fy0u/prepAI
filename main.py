import os
import threading
import time
import requests
import feedparser
import newspaper
from fastapi import FastAPI
from typing import Optional

# -------- Ollama host ----------
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")

# -------- Feeds (you can modify) ----------
FEEDS = [
    "https://feeds.bbci.co.uk/news/rss.xml",
    "https://www.thehindu.com/news/national/feeder/default.rss",
    "https://indianexpress.com/section/india/feed/",
    "https://www.livemint.com/rss/news",
    "https://www.business-standard.com/rss/latest.rss"
]

# -------- Scraping Helpers ----------
def fetch_feed_entries(feed_url, limit=5):
    d = feedparser.parse(feed_url)
    items = []
    for e in d.entries[:limit]:
        items.append({
            "title": e.get("title",""),
            "link": e.get("link",""),
            "published": e.get("published","")
        })
    return items

def extract_article(url):
    try:
        art = newspaper.Article(url)
        art.download()
        art.parse()
        return {
            "title": art.title,
            "authors": art.authors,
            "publish_date": art.publish_date.isoformat() if art.publish_date else "",
            "text": art.text,
            "url": url
        }
    except Exception as e:
        return {"error": str(e), "url": url}

def get_latest_articles():
    results = []
    for feed in FEEDS:
        for item in fetch_feed_entries(feed, limit=5):
            article = extract_article(item["link"])
            if article.get("text"):
                article["feed_title"] = item["title"]
                article["feed_published"] = item["published"]
                results.append(article)
    return results

# -------- UPSC Format ----------
UPSC_PROMPT = """You are an assistant generating UPSC Current Affairs notes.
Output strictly in this template:

Title:
Source/Date:
Why in News:
Key Facts (3-6 bullet points):
GS Paper Mapping: (GS I/II/III/IV + brief rationale)
Relevance/Implications (2-4 bullets):
Schemes/Acts/International (if applicable):
Prelims Pointers (2-4 bullets):
Mains Practice Question:

Keep it concise and exam-oriented. Do not include unrelated content.
"""

def ollama_generate(prompt, model="llama3.2"):
    r = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=180
    )
    r.raise_for_status()
    return r.json()["response"]

def to_upsc_note(article):
    title = article.get("title","")
    text = article.get("text","")
    url = article.get("url","")
    pub = article.get("publish_date") or article.get("feed_published") or ""
    source_line = f"{url} | {pub}"
    prompt = f"""{UPSC_PROMPT}

Article Title: {title}
Source & Date: {source_line}

Article Content:
{text}
"""
    return ollama_generate(prompt)

def build_daily_current_affairs(n_items=5):
    articles = get_latest_articles()
    articles = [a for a in articles if a.get("text")]
    articles.sort(key=lambda x: len(x["text"]), reverse=True)
    notes = []
    for art in articles[:n_items]:
        note = to_upsc_note(art)
        notes.append(note)
    return notes

# -------- FastAPI App ----------
app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/daily")
def daily(n: Optional[int]=5, model: Optional[str]="llama3.2"):
    # allow model override if you run a different one on Render or local
    global ollama_generate
    def ollama_generate_override(prompt, model=model):
        r = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={"model": model, "prompt": prompt, "stream": False},
            timeout=180
        )
        r.raise_for_status()
        return r.json()["response"]
    # temporarily bind in this scope
    orig = ollama_generate
    ollama_generate = ollama_generate_override
    try:
        notes = build_daily_current_affairs(n_items=min(max(int(n),1),10))
        return {"count": len(notes), "notes": notes}
    finally:
        ollama_generate = orig

# Optional: serve a basic homepage for your frontend (if needed)
@app.get("/")
def root():
    return {"message": "UPSC Current Affairs API. Use /daily?n=5 or open your static frontend."}
"""
