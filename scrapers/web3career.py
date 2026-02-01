from scrapers.base import BaseScraper
from utils.http import fetch
from models.job import Job

class Web3CareerScraper(BaseScraper):
    source = "web3career"

    def build_url(self, keyword: str) -> str:
        return f"https://web3.career/-jobs?keyword={keyword}"

    def fetch(self, keyword: str) -> str:
        return get_html(self.build_url(keyword))

    def parse(self, html: str) -> List[Job]:
        return []