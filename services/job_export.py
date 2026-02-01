from datetime import datetime
from typing import List

from models.job import Job
from utils.file_export import export_csv

FIELDNAMES = ["title", "company", "location", "salary", "link", "source", "tags", "description"]

def _safe_slug(text: str) -> str:
    text = (text or "").strip().lower()
    return "".join(ch if ch.isalnum() or ch in "-_" else "_" for ch in text) or "jobs"

def export_jobs_csv(jobs: List[Job], keyword: str) -> str:
    rows = []
    for job in jobs:
        tags = job.extra.get("tags") if job.extra else None
        if isinstance(tags, list):
            tags = " | ".join(tags)

        rows.append({
            "title": job.title,
            "company": job.company,
            "location": job.location or "",
            "salary": job.salary or "",
            "link": job.link or "",
            "source": job.source,
            "tags": tags or "",
            "description": (job.extra.get("description") if job.extra else "") or "",
        })

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_stem = f"{_safe_slug(keyword)}_{stamp}"
    return export_csv(rows, file_stem, FIELDNAMES)
