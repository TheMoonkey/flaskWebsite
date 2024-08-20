from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)


@app.route('/')
def helloWorld():
  return "Hello Word!"


if __name__ == '__main__':
  app.run(debug=True)
