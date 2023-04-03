#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response
#g is an object that can be used to store anything that you want to 
#store globally for the lifetime of a request.  it is reset
#with each new request

#session is a dictionary object that can be used to hold onto 
#valuses between multiple requests
import os

app = Flask(__name__)

@app.before_request
def app_path():
    #sets the variable g.path to the absolute path of the cu
    #rrent working directory
    #getcwd=get current working directory.  in short the line
    #below sets the g.path to the abs path of the cwd
    g.path =os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body= f'''<h1>The host for this page is {host}</h1>
            <h2>The name of this application is {appname}</h2>
            <h3>The path of this application on the user's device is {g.path}</h3>'''

    status_code =200
    headers = {}
    #using make_response will not change what we see in the browser
    #but it will make code cleaner and easier to replicate
    #and even automate in other views
    return make_response(response_body, status_code, headers)


#hooks: hooks are best implemented as decorators.  There are four
#types of hooks:
    #1. @app.before_request
    #2. @app.before_first_request
    #3. @app.after_request
    #4. @app.teardown_request

#using redirect() and abort()
    #use redirect() if the URL has changed
    #use abort to inform users that the resource does not exist 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
