"""
Project 07: Web Scraping - Practice Stubs

TODO: Implement web scraping functions
Run tests with: pytest test_solution.py -v
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict


def fetch_page(url: str) -> str:
    """
    Fetch HTML content from URL.

    Args:
        url: Website URL to fetch

    Returns:
        HTML content as string

    Raises:
        requests.RequestException: On network error
    """
    # TODO: Use requests.get() with error handling
    pass


def parse_html(html: str) -> BeautifulSoup:
    """
    Parse HTML string into BeautifulSoup object.

    Args:
        html: HTML content

    Returns:
        BeautifulSoup object
    """
    # TODO: Create BeautifulSoup object
    pass


def extract_links(soup: BeautifulSoup) -> List[str]:
    """
    Extract all links from HTML.

    Args:
        soup: BeautifulSoup object

    Returns:
        List of URLs (href attributes)
    """
    # TODO: Find all <a> tags and extract href
    pass


def extract_text_by_class(soup: BeautifulSoup, class_name: str) -> List[str]:
    """
    Extract text from elements with specific class.

    Args:
        soup: BeautifulSoup object
        class_name: CSS class name

    Returns:
        List of text content
    """
    # TODO: Find elements by class and extract text
    pass


def scrape_table(html: str) -> List[Dict[str, str]]:
    """
    Scrape data from HTML table.

    Args:
        html: HTML containing a <table>

    Returns:
        List of dictionaries (one per row)
    """
    # TODO: Parse table headers and rows
    pass


if __name__ == "__main__":
    # Test with example HTML
    html = """
    <html>
        <body>
            <h1 class="title">Test Page</h1>
            <a href="https://example.com">Link</a>
        </body>
    </html>
    """
    soup = parse_html(html)
    print("Links:", extract_links(soup))
