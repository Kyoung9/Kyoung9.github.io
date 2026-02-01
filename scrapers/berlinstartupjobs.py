from typing import List
from bs4 import BeautifulSoup

from scrapers.base import BaseScraper
from utils.http import get_html
from models.job import Job


class BerlinStartupJobsScraper(BaseScraper):
    source = "berlinstartupjobs"

    def build_url(self, keyword: str) -> str:
        return f"https://berlinstartupjobs.com/skill-areas/{keyword}/"

    def fetch_url(self, url: str) -> str:
        return get_html(url)

    def parse(self, html: str) -> List[Job]:
        soup = BeautifulSoup(html, "html.parser")
        list_root = soup.find("ul", class_="jobs-list-items")
        if not list_root:
            return []
        items = list_root.find_all("li")

        jobs = []
        for item in items:
            title_tag = item.select_one("h4.bjs-jlid__h a")
            company_tag = item.select_one("a.bjs-jlid__b")
            desc_tag = item.select_one("div.bjs-jlid__description")

            if not title_tag or not company_tag:
                continue
            
            category_list = [a.get_text(strip=True) for a in item.select("div.links-box a")]

            jobs.append(
                Job(
                    title = title_tag.get_text(strip = True), 
                    company = company_tag.get_text(strip = True), 
                    link = title_tag["href"], 
                    source = self.source,
                    extra = {"tags" : category_list, 
                    "description" : desc_tag.get_text(" ", strip=True) if desc_tag else None}
                )
            )
        return jobs
    