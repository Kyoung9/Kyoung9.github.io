from abc import ABC, abstractmethod
from typing import List
from models.job import Job

class BaseScraper(ABC):
    source: str

    @abstractmethod
    def build_url(self, keyword: str) -> str:
        pass

    @abstractmethod
    def fetch(self, term:str) -> str:
        pass

    @abstractmethod
    def parse(self, html:str) -> List[Job]:
        pass
    
    def search(self, keyword:str) -> List[Job]:
        html = self.fetch(keyword)
        return self.parse(html)