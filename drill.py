# Import dependencies
from flask import Flask
# Create a new Flask App Instance (__name__ is a "magic method")
app = Flask(__name__)
# define the starting point, the root
@app.route('/')
def hello_world():
	return 'Hello world'

# Run in terminal in folder: export FLASK_APP=app.py
# Then flask run 
# outputs: Running on http://xxx.x.x.x:xxxx/
# That's the localhost address and a port number (last four digits)
# enter localhost:<host> into browser as example below:
# localhost:5000 (most common local host)
# output in browser is hello world

# ----

# SKILL DRILL
# Think of some simple code from which you could create a route. 
# Then try to create a new route implementing that logic.

# Import dependencies
from flask import Flask
# Create a new Flask App Instance (__name__ is a "magic method")
app = Flask(__name__)
# define the starting point, the root. Above that add default name.
@app.route('/')
def skill_drill():
	return "What is the point of this?" * 5

# Run in terminal in folder: export FLASK_APP=drill.py
# Then flask run 
# outputs: Running on http://xxx.x.x.x:xxxx/
# That's the localhost address and a port number (last four digits)
# enter localhost:<host> into browser as example below:
# localhost:5000 (most common local host)
# output in browser is hello world