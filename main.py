from flask import Flask #imports Flask, the module we're gonna be using for the web server
app = Flask(__name__) #sets the "app" variable to a Flask instance
@app.route('/') #uses the app.route decorator with the argument "/" for the url path
def index(): #defines index, this can be named whatever you want
  return 'Hello world!' #returns 'Hello world!' to the user
app.run('0.0.0.0',8080) #starts the app!