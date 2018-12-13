from flask import Flask
#from config import Configuration


app = Flask(__name__)
#app.config.from_object(Configuration)
#from module import models
class Configuration(object):
    DEBUG=True
from dl import views
