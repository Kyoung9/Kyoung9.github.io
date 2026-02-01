from abc import ABC, abstractmethod
from typing import List, Optional

from models.job import Job


class BaseScraper(ABC):
    source: str = ""

    @abstractmethod
    def build_url(self, keyword: str) -> str:
        raise NotImplementedError

    def build_page_url(self, keyword: str, page: int) -> str:
        if page == 1:
            return self.build_url(keyword)
        raise NotImplementedError("Override build_page_url for page pagination.")

    @abstractmethod
    def fetch_url(self, url: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def parse(self, html: str) -> List[Job]:
        raise NotImplementedError

    def search(self, keyword: str) -> List[Job]:
        html = self.fetch_url(self.build_url(keyword))
        return self.parse(html)

    def search_by_page_param(self, keyword: str, max_pages: int = 20) -> List[Job]:
        results: List[Job] = []
        for page in range(1, max_pages + 1):
            html = self.fetch_url(self.build_page_url(keyword, page))
            jobs = self.parse(html)
            if not jobs:
                break
            results.extend(jobs)
        return results

    def next_page_url(self, html: str) -> Optional[str]:
        return None

    def search_by_next_link(self, keyword: str, max_pages: int = 20) -> List[Job]:
        results: List[Job] = []
        url = self.build_url(keyword)
        for _ in range(max_pages):
            html = self.fetch_url(url)
            jobs = self.parse(html)
            if not jobs:
                break
            results.extend(jobs)
            url = self.next_page_url(html)
            if not url:
                break
        return results
