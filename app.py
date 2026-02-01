from flask import Flask, render_template, request, redirect, send_file

from utils.cache import TTLCache
from services.job_search import JobSearchService
from services.job_export import export_jobs_csv

app = Flask("JobScrapper")
cache = TTLCache()
service = JobSearchService()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")

    cached = cache.get(keyword)
    if cached:
        jobs = cached
    else:
        jobs = service.search(keyword)
        cache.set(keyword, jobs)
        
    return render_template("search.html", jobs = jobs, keyword = keyword)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if not keyword:
        return redirect("/")
    jobs = _get_jobs(keyword)
    file_path = export_jobs_csv(jobs, keyword)
    return send_file(file_path, as_attachment=True)


def _get_jobs(keyword: str):
    cached = cache.get(keyword)
    if cached:
        return cached
    jobs = service.search(keyword)
    cache.set(keyword, jobs)
    return jobs




if __name__ == "__main__":
    # app.run("0.0.0.0")
    app.run(port = 5001)