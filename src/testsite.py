import time
import ssl
import sys
import flask
from flask import jsonify, request

app = flask.Flask(__name__)
# Create some test data for our catalog in the form of a list of dictionaries.
applicants = [
    {
     'Last': 'Guy',
     'First': 'Grumpy',
     'Position': 'Software Development Intern',
     'School': 'University of Maryland',
     'Program': 'Rage Studies'
     },
    {
     'Last': 'Doc',
     'First': 'Tiny',
     'Position': 'Software Development Intern',
     'School': 'Academy for Small Doctors',
     'Program': 'Princess Revival'},
    {
     'Last': 'Happy',
     'First': 'Mister',
     'Position': 'Happiness Analyst',
     'School': 'Lumberjack Academy',
     'Program': 'Smiling at Strangers'
     },
    {
     'Last': 'Boy',
     'First': 'Bashful',
     'Position': 'Software Development Intern',
     'School': 'UMBC',
     'Program': 'Avoiding Strangers'
     },
    {
     'Last': 'Sneezy',
     'Program': 'Hip-Hop',
     'First': 'Lil',
     'Position': 'Software Development Intern',
     'School': 'Julliard'
     },
    {
     'Last': 'Dumps',
     'First': 'Dopey',
     'Position': 'Software Development Intern',
     'School': 'Montgomery College',
     'Program': 'Electrical Engineering'
     },
    {'Last': 'Sleepy',
     'First': 'Sir',
     'School': 'New York University',
     'Position': 'Software Development Intern',
     'Program': 'Architecture'},

]

# error page
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

# main page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Applicants</h1>
		<p>MapMG Intern Test.</p>'''


# API route that hosts json data
@app.route('/api/v1/resources/applicants/all', methods=['GET'])
def api_all():
    return jsonify(applicants)

app.run()
