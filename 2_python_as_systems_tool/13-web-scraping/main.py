"""
Project 07: Web Scraping - Demo
"""

from solution import parse_html, extract_links, extract_text_by_class, scrape_table


def demo_basics():
    print("=" * 70)
    print("DEMO 1: Basic HTML Parsing")
    print("=" * 70)

    html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Welcome!</h1>
            <p class="intro">This is a test page.</p>
            <a href="https://python.org">Python</a>
            <a href="https://github.com">GitHub</a>
        </body>
    </html>
    """

    soup = parse_html(html)
    print(f"Title: {soup.title.text}")
    print(f"H1: {soup.find('h1').text}")
    print()


def demo_extract_links():
    print("=" * 70)
    print("DEMO 2: Extract Links")
    print("=" * 70)

    html = """
    <html>
        <body>
            <a href="https://python.org">Python</a>
            <a href="https://github.com">GitHub</a>
            <a href="/about">About</a>
        </body>
    </html>
    """

    soup = parse_html(html)
    links = extract_links(soup)
    print("Found links:")
    for link in links:
        print(f"  - {link}")
    print()


def demo_extract_by_class():
    print("=" * 70)
    print("DEMO 3: Extract by CSS Class")
    print("=" * 70)

    html = """
    <html>
        <body>
            <p class="price">$19.99</p>
            <p class="description">Product info</p>
            <p class="price">$29.99</p>
            <p class="price">$39.99</p>
        </body>
    </html>
    """

    soup = parse_html(html)
    prices = extract_text_by_class(soup, "price")
    print("Prices found:")
    for price in prices:
        print(f"  - {price}")
    print()


def demo_scrape_table():
    print("=" * 70)
    print("DEMO 4: Scrape Table Data")
    print("=" * 70)

    html = """
    <table>
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Stock</th>
        </tr>
        <tr>
            <td>Laptop</td>
            <td>$999</td>
            <td>15</td>
        </tr>
        <tr>
            <td>Mouse</td>
            <td>$29</td>
            <td>50</td>
        </tr>
    </table>
    """

    data = scrape_table(html)
    print("Table data:")
    for row in data:
        print(f"  {row}")
    print()


def main():
    print("\n🌐" * 35)
    print("  PROJECT 07: WEB SCRAPING")
    print("🌐" * 35)
    print()

    demo_basics()
    demo_extract_links()
    demo_extract_by_class()
    demo_scrape_table()

    print("=" * 70)
    print("Key Takeaways:")
    print("1. Use requests for HTTP, BeautifulSoup for parsing")
    print("2. find() and find_all() for element selection")
    print("3. CSS selectors for specific elements")
    print("4. Always handle network errors")
    print("5. Respect robots.txt and rate limits!")
    print()


if __name__ == "__main__":
    main()
