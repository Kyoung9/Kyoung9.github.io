import logging
from typing import List, Set

from models.job import Job
from scrapers.berlinstartupjobs import BerlinStartupJobsScraper
from scrapers.weworkremotely import WeWorkRemotelyScraper
from scrapers.web3career import Web3CareerScraper

logger = logging.getLogger(__name__)


class JobSearchService:
    def __init__(self, scrapers=None):
        if scrapers is None:
            scrapers = [
                BerlinStartupJobsScraper(),
                WeWorkRemotelyScraper(),
                Web3CareerScraper(),
            ]
        self.scrapers = scrapers

    def search(self, keyword: str) -> List[Job]:
        keyword = (keyword or "").strip()
        if not keyword:
            return []

        results: List[Job] = []
        for scraper in self.scrapers:
            try:
                results.extend(scraper.search(keyword))
            except Exception:
                source = getattr(scraper, "source", scraper.__class__.__name__)
                logger.exception("Scraper failed: %s", source)

        return self._dedupe(results)

    #중복 제거
    @staticmethod
    def _dedupe(jobs: List[Job]) -> List[Job]:
        seen: Set[str] = set()
        deduped: List[Job] = []
        for job in jobs:
            key = job.link or f"{job.source}|{job.company}|{job.title}"
            if key in seen:
                continue
            seen.add(key)
            deduped.append(job)
        return deduped


def extract_jobs(keyword: str) -> List[Job]:
    return JobSearchService().search(keyword)
