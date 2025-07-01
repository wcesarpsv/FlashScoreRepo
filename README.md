# ⚽ Football Odds Scraper (FlashScore)

A lightweight Python scraper to collect football match odds and basic match data using Selenium.

### ✅ What it collects

- Match ID
- League
- Time
- Home Team
- Away Team
- Full-time Odds (Home / Draw / Away)

---

### 🚀 Getting Started

#### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 2. Run the Scraper

```bash
python scraper.py
```

It will scrape data for the first 100 matches and save it to:

```
simplified_matches.csv
```

---

### 🔧 Requirements

- Python 3.8+
- Chrome browser installed
- ChromeDriver (compatible with your Chrome version)

> Tip: You can simplify setup by using `webdriver-manager`.

---

### 🧠 Build On It

This is a minimal template to start scraping football odds.
You can expand it to:

- Add Over/Under, BTTS, and Handicap odds
- Scrape multiple pages or historical data
- Export to a database or automate daily jobs

---

### 📄 License

MIT — open for contribution and learning!
