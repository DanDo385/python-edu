"""
Project 07: Web Scraping - Tests
"""

import pytest
from solution import (
    parse_html,
    extract_links,
    extract_text_by_class,
    scrape_table
)


class TestParseHTML:
    def test_parse_simple_html(self):
        html = "<html><body><h1>Test</h1></body></html>"
        soup = parse_html(html)
        assert soup.find('h1').text == "Test"


class TestExtractLinks:
    def test_extract_links(self):
        html = """
        <html>
            <body>
                <a href="https://example.com">Link 1</a>
                <a href="/page2">Link 2</a>
            </body>
        </html>
        """
        soup = parse_html(html)
        links = extract_links(soup)
        assert len(links) == 2
        assert "https://example.com" in links


class TestExtractTextByClass:
    def test_extract_by_class(self):
        html = """
        <html>
            <body>
                <p class="highlight">Text 1</p>
                <p>Other text</p>
                <p class="highlight">Text 2</p>
            </body>
        </html>
        """
        soup = parse_html(html)
        texts = extract_text_by_class(soup, "highlight")
        assert texts == ["Text 1", "Text 2"]


class TestScrapeTable:
    def test_scrape_simple_table(self):
        html = """
        <table>
            <tr><th>Name</th><th>Age</th></tr>
            <tr><td>Alice</td><td>30</td></tr>
            <tr><td>Bob</td><td>25</td></tr>
        </table>
        """
        data = scrape_table(html)
        assert len(data) == 2
        assert data[0] == {"Name": "Alice", "Age": "30"}
        assert data[1] == {"Name": "Bob", "Age": "25"}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
