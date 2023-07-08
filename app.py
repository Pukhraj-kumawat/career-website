from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/job/<id>")
def show_job(id):
  try:
    job_res = load_job_from_db(id)
    return render_template('jobpage.html', job=job_res)
  except Exception as e:
    return "Not found 404"


@app.route("/api/jobs")
def get_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
