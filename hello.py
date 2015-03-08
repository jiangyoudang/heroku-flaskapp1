import os

from init import app
from flask import render_template
from flask import jsonify
import json
from database import database

@app.route("/")
def hello():
    # return app.send_static_file('templates/base.html')
    return render_template('resume.html')

@app.route('/userlist')
def get_user_list():
    d = database.getUsers()
    # result = json.dumps(d)
    # return result

    return render_template('base.html', users = d)

#############
# with angular js

@app.route('/ng')
def ng_index():
    return app.send_static_file('index.html')

#
# @app.route('/add')
# def add_user():
#
#     db.insert('users', {'name':'test','email':'test@scu'})
#     return 'Done'

if __name__ == "__main__":
    app.run(debug=True)
