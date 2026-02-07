# PrepAI - Smart Current Affairs Tutor 📰

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()

> An intelligent current affairs platform designed specifically for UPSC, SSC, CDS, and PCS exam aspirants.

## 🎯 Overview

PrepAI is a comprehensive AI-powered current affairs tutor that helps competitive exam aspirants stay updated with relevant news and developments. It automatically curates, summarizes, and presents news in an exam-oriented format, saving valuable preparation time.

## ✨ Key Features

### 📝 Intelligent News Curation
- **Automated Source Aggregation:** Pulls news from trusted sources relevant to competitive exams
- **Smart Filtering:** Filters out irrelevant content, focusing on exam-relevant topics
- **Topic Categorization:** Organizes news by subject areas (Polity, Economy, Environment, etc.)

### 🎓 Exam-Oriented Content
- **Concise Summaries:** Delivers bite-sized, easy-to-revise news summaries
- **Background Context:** Provides historical context and related information
- **Key Points Highlighting:** Emphasizes exam-relevant facts and figures
- **Previous Year Connections:** Links current affairs to past exam questions

### 💡 Interactive Learning
- **Practice Questions:** AI-generated MCQs based on current news
- **Explanation Mode:** Detailed explanations for better understanding
- **Revision Notes:** Downloadable summary sheets for quick revision
- **Daily Digest:** Curated daily updates delivered to your email (optional)

### 📊 Progress Tracking
- **Reading History:** Track which topics you've covered
- **Quiz Performance:** Monitor your practice test scores
- **Weak Areas:** Identify topics that need more attention
- **Custom Alerts:** Set notifications for specific subjects or topics

## 🚀 Technology Stack

- **Backend:** Python 3.8+
- **AI/NLP:** Natural Language Processing for text summarization
- **Web Scraping:** BeautifulSoup, Selenium
- **Database:** SQLite/PostgreSQL
- **Frontend:** HTML, CSS, JavaScript (if web-based)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

```bash
# Clone the repository
git clone https://github.com/W0nder0fy0u/prepAI.git
cd prepAI

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Initialize database
python setup_db.py

# Run the application
python main.py
```

## 🎮 Usage

### Basic Usage

```python
# Example: Fetch today's news
from prepai import CurrentAffairs

ca = CurrentAffairs()
today_news = ca.get_daily_digest()

# Get news by category
polity_news = ca.get_by_category('Polity')

# Generate practice questions
questions = ca.generate_quiz(topic='Economy', count=10)
```

### Command Line Interface

```bash
# Fetch and display today's news
python prepai.py --fetch-today

# Get news for specific category
python prepai.py --category "International Relations"

# Generate quiz
python prepai.py --quiz --topic "Environment" --questions 10

# Export daily digest
python prepai.py --export --format pdf
```

## 📚 Project Structure

```
prepAI/
├── src/
│   ├── scraper/          # News scraping modules
│   ├── nlp/              # NLP and summarization
│   ├── database/         # Database models and operations
│   ├── quiz/             # Question generation
│   └── utils/            # Utility functions
├── data/
│   ├── sources.json      # News source configuration
│   ├── categories.json   # Topic categories
│   └── keywords.json     # Exam-relevant keywords
├── tests/                # Unit and integration tests
├── docs/                 # Documentation
├── requirements.txt      # Python dependencies
├── config.py            # Configuration settings
└── main.py              # Application entry point
```

## 🔧 Configuration

Edit `config.py` or `.env` file to customize:

```python
# News sources
NEWS_SOURCES = ['The Hindu', 'Indian Express', 'PIB']

# Update frequency
UPDATE_INTERVAL = 'daily'  # or 'hourly'

# Summary length
SUMMARY_MAX_WORDS = 150

# Categories to track
CATEGORIES = ['Polity', 'Economy', 'Environment', 'International Relations']
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Write unit tests for new features
- Update documentation as needed
- Ensure all tests pass before submitting PR

## 📝 Future Enhancements

- [ ] Mobile application (Android/iOS)
- [ ] Multi-language support (Hindi, regional languages)
- [ ] Voice-based news summaries
- [ ] AI-powered personalized study plans
- [ ] Integration with popular exam prep platforms
- [ ] Offline mode for downloaded content
- [ ] Social features (study groups, peer discussions)

## 🐛 Known Issues

- News scraping may be slow during peak hours
- Some PDF exports may have formatting issues
- Quiz generation accuracy being improved

Please report issues [here](https://github.com/W0nder0fy0u/prepAI/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Subham Tiwari**
- GitHub: [@W0nder0fy0u](https://github.com/W0nder0fy0u)
- Email: [](mailto:)

## 🙏 Acknowledgments

- Thanks to all the open-source libraries used in this project
- Inspired by the needs of millions of competitive exam aspirants
- Special thanks to contributors and testers

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a ⭐ on GitHub!

---

**Built with ❤️ for UPSC, SSC, CDS, and PCS aspirants**

*Last Updated: February 2026*
