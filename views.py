#! /usr/bin/env python3
from blueprints.catagories import catagory
from blueprints.owners import owner
from flask import Blueprint, Flask
app = Flask(__name__)

@app.route('/')
@app.route('/catalog/')
def homepage():
  return "Homepage!"

app.register_blueprint(owner, url_prefix='/catalog/owner')
app.register_blueprint(catagory, url_prefix='/catalog/catagory')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
