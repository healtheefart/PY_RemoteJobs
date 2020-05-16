from flask import Flask, render_template, request, redirect, send_file
from scrapper import so_scrapper, wwr_scrapper, ro_scrapper
from exporter import save_to_file
import csv

app = Flask("RemoteJobs")
fakeDB = {}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  search_language = request.args.get('term',None).lower()
  fromDB = fakeDB.get(search_language)
  if fromDB:
    jobs_list = fromDB
    num_of_jobs = len(jobs_list)
  else:
    SO_url = f"https://stackoverflow.com/jobs?r=true&q={search_language}"
    WWR_url = f"https://weworkremotely.com/remote-jobs/search?term={search_language}"
    RO_url = f"https://remoteok.io/remote-dev+{search_language}-jobs"
    jobs_list = []
    jobs_list = jobs_list + so_scrapper(SO_url) + wwr_scrapper(WWR_url) + ro_scrapper(RO_url)
    num_of_jobs = len(jobs_list)
    fakeDB[f"{search_language}"] = jobs_list
  return render_template("search.html", jobs_list = jobs_list, search_language = search_language, num_of_jobs = num_of_jobs)

@app.route("/export")
def export():
  try:
    search_language = request.args.get('term',None)
    if not search_language:
      raise Exception()
    search_language = search_language.lower()
    jobs = fakeDB.get(search_language)
    if not jobs:
      raise Exception()
    save_to_file(jobs, search_language)
    file_name = f"{search_language}.csv"
    return send_file(file_name,mimetype='text/csv', attachment_filename=f'{search_language}.csv', as_attachment=True)
  except:
    return redirect("/")

app.run(host="0.0.0.0")