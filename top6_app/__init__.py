from flask import Flask

app = Flask(__name__)

from top6_app import routes
