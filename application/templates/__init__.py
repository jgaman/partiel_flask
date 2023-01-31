from flask import Flask

app = Flask(__name__)

from application.templates import routes
