import os

from init import app
from flask import render_template
from flask import jsonify
import json
from database import model

@app.route("/")
def hello():
    return app.send_static_file('templates/base.html')


# @app.route('/userlist')
# def get_user_list():
#     d = db.get_user()
#     # result = json.dumps(d)
#     # return result
#     return jsonify(users = d)
#
# @app.route('/add')
# def add_user():
#
#     db.insert('users', {'name':'test','email':'test@scu'})
#     return 'Done'

if __name__ == "__main__":
    app.run(debug=True)
