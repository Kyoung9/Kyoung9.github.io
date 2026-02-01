from typing import List
from bs4 import BeautifulSoup
import re

from scrapers.base import BaseScraper
from utils.http import get_html
from models.job import Job


class WeWorkRemotelyScraper(BaseScraper):
    source = "weworkremotely"

    def build_url(self, keyword: str) -> str:
        return f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={keyword}"

    def fetch_url(self, url: str) -> str:
        return get_html(url)

    def parse(self, html: str) -> List[Job]:
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select("section.jobs li.new-listing-container")
        if not items:
            return []
        
        jobs = []
        for item in items:
            title_tag = item.select_one("h3.new-listing__header__title")
            company_tag = item.select_one("p.new-listing__company-name")
            location_tag = item.select_one("p.new-listing__company-headquarters")
            link_tag = item.select_one("a.listing-link--unlocked")

            if not title_tag or not company_tag:
                continue
            
            categories = [
                t.get_text(strip=True)
                for t in item.select("div.new-listing__categories p.new-listing__categories__category")
                if t.get_text(strip=True) != "Top 100"
            ]

            salary = None
            category_list = []
            for c in categories:
                if re.search(r"\$\d", c):
                    salary = c
                else:
                    category_list.append(c)

            jobs.append(
                Job(
                    title = title_tag.get_text(strip = True), 
                    company = company_tag.get_text(strip = True), 
                    location = location_tag.get_text(strip = True) if location_tag else None,
                    link = f'https://weworkremotely.com{link_tag["href"]}'if link_tag else None, 
                    salary = salary,
                    source = self.source,
                    extra = {"tags" : category_list}
                )
            )
        return jobs
    
