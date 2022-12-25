from flask import Flask, render_template, request, redirect, send_file
from extractors.albamon import get_albamon_jobs
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/search')
def search():
    albamon = get_albamon_jobs()
    return render_template("search.html", keyword="알바", jobs=albamon)