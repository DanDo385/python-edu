"""
PROJECT 07: WEB SCRAPING

Web scraping extracts data from websites. This is useful for:
- Price monitoring
- Data aggregation
- Research
- Automation

IMPORTANT: Always respect robots.txt and terms of service!
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def fetch_page(url: str) -> str:
    """Fetch HTML content from URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise exception for 4xx/5xx
        return response.text
    except requests.RequestException as e:
        raise Exception(f"Failed to fetch {url}: {e}")


def parse_html(html: str) -> BeautifulSoup:
    """Parse HTML into BeautifulSoup object."""
    return BeautifulSoup(html, 'html.parser')


def extract_links(soup: BeautifulSoup) -> List[str]:
    """Extract all links from HTML."""
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links


def extract_text_by_class(soup: BeautifulSoup, class_name: str) -> List[str]:
    """Extract text from elements with specific class."""
    elements = soup.find_all(class_=class_name)
    return [elem.get_text(strip=True) for elem in elements]


def scrape_table(html: str) -> List[Dict[str, str]]:
    """Scrape data from HTML table."""
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        return []

    # Extract headers
    headers = []
    header_row = table.find('tr')
    if header_row:
        headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]

    # Extract rows
    rows = []
    for tr in table.find_all('tr')[1:]:  # Skip header row
        cells = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
        if cells and headers:
            row_dict = dict(zip(headers, cells))
            rows.append(row_dict)

    return rows


# BEST PRACTICES:
# ---------------
# 1. Respect robots.txt
# 2. Add delays between requests (time.sleep)
# 3. Use User-Agent header
# 4. Handle errors gracefully
# 5. Cache responses when possible
