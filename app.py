#import flask
from flask import Flask, render_template, jsonify

JOBS = [{
  'id': 1,
  'location': 'Bengaluru',
  'Designation': 'Geospatial Engineer',
  'Salary': 'Rs.45000'
}, {
  'id': 2,
  'location': 'Chennai',
  'Designation': 'Geospatial Developer',
  'Salary': 'Rs.50000'
}, {
  'id': 3,
  'location': 'Hyderabad',
  'Designation': 'Geospatial Trainer',
  'Salary': 'Rs.50000'
}, {
  'id': 4,
  'location': 'Delhi',
  'Designation': 'Drone Pilot',
  'Salary': 'Rs.30000'
}]
app = Flask(__name__)


@app.route('/')
def hello_haseeb():
  return render_template('home.html', jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
