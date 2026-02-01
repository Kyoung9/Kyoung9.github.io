from typing import List
from bs4 import BeautifulSoup

from scrapers.base import BaseScraper
from utils.http import get_html
from models.job import Job


class Web3CareerScraper(BaseScraper):
    source = "web3career"

    def build_url(self, keyword: str) -> str:
        return f"https://web3.career/{keyword}-jobs"

    def build_page_url(self, keyword: str, page: int) -> str:
        base = self.build_url(keyword)
        return base if page == 1 else f"{base}?page={page}"

    def fetch_url(self, url: str) -> str:
        return get_html(url)

    def search(self, keyword: str) -> List[Job]:
        return self.search_by_page_param(keyword, max_pages=20)

    def parse(self, html: str) -> List[Job]:
        soup = BeautifulSoup(html, "html.parser")
        items = soup.select("div.row-cols-2 table tr.table_row")
        if not items:
            return []
        
        jobs = []
        for item in items:
            link_tag = item.select_one("div.job-title-mobile a")
            title_tag = item.select_one("div.job-title-mobile a h2")
            company_tag = item.select_one("td.job-location-mobile h3")
            location_tag = item.select_one("td.job-location-mobile a")
            salary_tag = item.select_one("p.text-salary")
            
            if not title_tag or not company_tag:
                continue
            
            category_list = [a.get_text(strip=True) for a in item.select("span.my-badge.my-badge-secondary a")]

            jobs.append(
                Job(
                    title = title_tag.get_text(strip = True), 
                    company = company_tag.get_text(strip = True), 
                    location = location_tag.get_text(strip = True) if location_tag else None,
                    link = f'https://web3.career{link_tag["href"]}'if link_tag else None, 
                    salary = salary_tag.get_text(strip = True) if salary_tag else None,
                    source = self.source,
                    extra = {"tags" : category_list}
                )
            )
        return jobs