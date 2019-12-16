.. _RST Overview:

Source Code Description
************************
The source code is made of two files, broken down below:

testsite.py posts a simple Flask app web page to mimic an active API.
It supplies 7 test cases in JSON format, found at '/api/v1/resources/applicants/all'
Run testsite.py first to post the test website, and leave it running to keep the
site open while you run sqlator.py, which scrapes the information from the site.

sqlator.py goes to the test site and pulls the JSON information.
The supplied URL can be replaced with a URL and queries from a real API,
provided it follows the formatting requirements for the defined sql table, listed in 'Database-Specification.'

The code supplies a list of available position, grabs the JSON info,
runs some error checks, then organizes the JSON data into a sql table: 'applicants.sqlite' with the specified columns.

Columns, in order, are: "First, Last, Position, Program, School, Time, id"
All of these keys, aside from the auto-generated time and id columns,
must be included in the JSON for the applicant to be included in the SQL table

Valid applicants are saved to a sqlite database.
Invalid entries and entries for unavailable positions are printed and skipped.


The 'Applicants.sqlite' file I provided is populated with test cases I ran previously, 
but a new sql table will be created on the first run of the program 
and updated each time the program is run. 
