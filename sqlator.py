import json
import ssl
import urllib.request
import sqlalchemy as db
# takes json input from test site defined in testsite.py
url = "http://127.0.0.1:5000/api/v1/resources/applicants/all"

# list of positions available to test against
avail_positions=['Software Development Intern']


# creating sql database
engine = db.create_engine('sqlite:///applicants.sqlite')
cur = engine.connect()

cur.execute(
    """CREATE TABLE IF NOT EXISTS applicants (First TEXT,
    Last TEXT,
    Position TEXT,
    Program TEXT,
    School TEXT,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    id INTEGER PRIMARY KEY AUTOINCREMENT)""")

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# opening API url
parms = dict()
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data))

# load data and read into applicants.sqlite
js = json.loads(data)
# looping through provided json packs and adding info one column at a time
for entry in js:
    columns = entry.keys()
    # integrity check
    if entry['Position'] not in avail_positions:
        print(entry)
        print('Ignored for unavailable position')
        continue

    cur.execute("""INSERT INTO applicants (%s,%s,%s,%s,%s)
                        VALUES (?,?,?,?,?)""" % (tuple(columns)), (tuple(entry.values()),))




