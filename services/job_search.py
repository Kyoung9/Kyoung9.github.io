import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class Job:
    title: str
    company: str
    location: str
    link: str

def extract_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    response = requests.get(f"{base_url}{keyword}")
    if response.status_code != 200:
        print("Failed to fetch jobs")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all("section", class_="jobs")
    return jobs