from scrapers.base import BaseScraper
from utils.http import fetch
from models.job import Job

class WeWorkRemotelyScraper(BaseScraper):
    source = "weworkremotely"

    def build_url(self, keyword: str) -> str:
        return f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"

    def fetch(self, keyword: str) -> str:
        return get_html(self.build_url(keyword))

    def parse(self, html: str) -> List[Job]:
        return []