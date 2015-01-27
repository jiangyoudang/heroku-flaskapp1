from flask import Flask
app = Flask(__name__)

from flask import render_template

########################
#route dispatch

import json
from database import db


@app.route("/")
def hello():
    return render_template('base.html', title='Home')



@app.route('/userlist')
def get_user_list():
    d = db.get_user()
    result = json.dumps(d)
    return result


if __name__ == "__main__":
    app.run()
