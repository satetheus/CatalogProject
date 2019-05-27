#! /usr/bin/env python3
from flask import Flask, Blueprint
from owners import owner
from catagories import catagory

app = Flask(__name__)
app.register_blueprint(owner, url_prefix='/catalog/owner')
app.register_blueprint(catagory, url_prefix='/catalog/catagory')

@app.route('/')
@app.route('/catalog')
def homepage():
  return "Homepage!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)