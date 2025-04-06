import requests
from bs4 import BeautifulSoup
import json
import csv

class scrapers:
    def __init__(self, user_agent):
        self.headers = {'User-Agent': user_agent}

    def fetch_html(self, url):
        response = requests.get(url, headers=self.headers)
        return response.text

    def parse_html(self, html, selector):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(selector)

    def get_status_code(self, url):
        return requests.get(url, headers=self.headers).status_code

    def get_title(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return soup.title.string if soup.title else None

    def get_meta_description(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tag = soup.find("meta", attrs={"name": "description"})
        return tag["content"] if tag else None

    def get_all_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return [tag.name for tag in soup.find_all()]

    def count_elements(self, html, tag):
        soup = BeautifulSoup(html, 'html.parser')
        return len(soup.find_all(tag))

    def get_raw_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def is_valid_url(self, url):
        return url.startswith("http")
