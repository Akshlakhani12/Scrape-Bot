# advanced_scraper.py
from Scraper import SimpleScraper
from bs4 import BeautifulSoup

class AdvancedScraper(SimpleScraper):
    def __init__(self, user_agent):
        super().__init__(user_agent)

    def fetch_multiple(self, urls):
        return [self.fetch_html(url) for url in urls]

    def fetch_and_parse(self, url, selector):
        html = self.fetch_html(url)
        return self.parse_html(html, selector)

    def get_all_links_from_url(self, url):
        html = self.fetch_html(url)
        elements = self.parse_html(html, "a")
        return [el.get("href") for el in elements if el.get("href")]

    def scrape_with_keywords(self, url, keyword):
        html = self.fetch_html(url)
        soup = self.get_raw_soup(html)
        return [el for el in soup.find_all() if keyword in str(el)]

    def print_elements(self, elements):
        for el in elements:
            print(el)

    def extract_table_data(self, html):
        soup = self.get_raw_soup(html)
        tables = soup.find_all("table")
        return [[cell.get_text(strip=True) for cell in row.find_all(["td", "th"])] for table in tables for row in table.find_all("tr")]

    def scrape_paginated(self, base_url, pages=5):
        data = []
        for i in range(1, pages + 1):
            html = self.fetch_html(f"{base_url}?page={i}")
            soup = self.get_raw_soup(html)
            data.append(soup.title.string if soup.title else "No Title")
        return data

    def override_example(self):
        return "This is overridden in AdvancedScraper"

    def example_polymorphism(self):
        return "From AdvancedScraper"

    def custom_headers(self):
        return self.headers
