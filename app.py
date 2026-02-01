from flask import Flask, render_template, request, redirect, send_file
from utils.cache import TTLCache
from services.job_search import extract_jobs

app = Flask("JobScrapper")
cache = TTLCache()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if cache.get(keyword):
        jobs = cache.get(keyword)
    else:
        jobs = extract_jobs(keyword)
        cache.set(keyword, jobs)
    return render_template("search.html")

if __name__ == "__main__":
    app.run("0.0.0.0")