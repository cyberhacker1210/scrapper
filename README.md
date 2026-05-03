# scrapper — Python Web Scraping Tool

A Python tool that automatically extracts data from websites. Useful for price tracking, data collection, content aggregation, or any automated data extraction task.

## Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Main language |
| BeautifulSoup4 | HTML parsing |
| Requests | HTTP requests |
| Selenium | Dynamic page scraping |
| Pandas | Data manipulation |
| CSV / JSON | Data export |

## How it works

```
Target URL provided
        ↓
HTTP GET request sent
        ↓
HTML parsed by BeautifulSoup
        ↓
Target data extracted
        ↓
Data cleaned and structured
        ↓
Exported to CSV or JSON
```

## Features

- Scrape static pages with Requests or dynamic pages with Selenium
- Extract prices, titles, links, images, and more
- Export results to CSV or JSON
- Configurable CSS/XPath selectors
- Rate limiting to avoid blocks

## Project Structure

```
scrapper/
├── main.py           # Entry point
├── scrapper.py       # Core scraping logic
├── parser.py         # HTML parsing functions
├── exporter.py       # CSV/JSON export
├── config.py         # URLs and selectors
├── requirements.txt
└── output/
    └── data.csv
```

## Getting Started

**Prerequisites:** Python 3.8+, pip, Chrome/Firefox (for Selenium)

```bash
git clone https://github.com/cyberhacker1210/scrapper
cd scrapper
pip install -r requirements.txt
```

Edit `config.py`:

```python
TARGET_URL = "https://example.com/products"
SELECTOR = ".product-price"
OUTPUT_FILE = "output/data.csv"
DELAY = 1  # seconds between requests
```

```bash
# Basic run
python main.py

# With custom arguments
python main.py --url "https://example.com" --selector ".price"

# Export as JSON
python main.py --format json
```

### Output example

```csv
title,price,url
"Product A","29.99€","https://..."
"Product B","49.99€","https://..."
```

> ⚠️ Always check a website's `robots.txt` and Terms of Service before scraping. Use responsibly and respect rate limits.

## Author

**cyberhacker1210** — [GitHub](https://github.com/cyberhacker1210)
