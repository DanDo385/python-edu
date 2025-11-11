# Project 07: 🌐 Web Scraping

> **Extract data from websites with requests and BeautifulSoup**

## 🎯 Real-World Skills

- HTTP requests with requests library
- HTML parsing with BeautifulSoup
- CSS selectors
- Error handling
- Data extraction patterns

## 📚 Example

```python
import requests
from bs4 import BeautifulSoup

response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')
titles = [h2.text for h2 in soup.find_all('h2')]
```

## 🏃 Run

```bash
python main.py && pytest test_solution.py -v
```

**Status:** ✅ Complete with real examples!
