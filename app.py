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

