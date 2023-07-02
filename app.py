from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'Id': 1,
  'Job-title': 'Front-end engineer',
  'Salary': 'Rs 25000',
  'Location': 'Mumbai'
}, {
  'Id': 2,
  'Job-title': 'Data analyst',
  'Salary': 'Rs 40000',
  'Location': 'Banguluru'
}, {
  'Id': 3,
  'Job-title': 'Back-end engineer',
  'Location': 'Delhi'
}, {
  'Id': 4,
  'Job-title': 'Cloud engineer',
  'Salary': 'Rs 24000',
  'Location': 'Remote'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/jobs")
def get_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
