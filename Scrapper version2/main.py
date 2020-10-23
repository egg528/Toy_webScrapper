from flask import Flask, render_template, request, redirect, send_file

import exporter
from Sok import get_jobs as get_Sok_jobs
from Indeed import get_jobs as get_Indeed_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}



#데코레이터(ex/ app.route)는 바로 아래에 있는 함수만 본다.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            Sok = get_Sok_jobs(word)
            Indeed = get_Indeed_jobs()
            jobs = Sok + Indeed
            db[word] = jobs

    else:
        redirect("/")
    return render_template("report.html", searchingBy = word, resultsNumber = len(jobs), jobs = jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

app.run(host="127.0.0.1")