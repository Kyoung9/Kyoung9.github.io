from scrapers.base import BaseScraper
from utils.http import fetch
from models.job import Job

class BerlinStartupJobsScraper(BaseScraper):
    sorce = "berlinstartupjobs"

    def build_url(self, keyword; str) -> str:
        return f"https://berlinstartupjobs.com/skill-areas/{keyword}"

    def getch(self, keyword: str) -> str:
        return get_html(self.build_url(keyword))

    def parse(self, html: str) -> List[Job]:
        return []