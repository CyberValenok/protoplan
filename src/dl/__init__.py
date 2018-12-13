from flask import Flask, render_template
#from config import Configuration


app = Flask(__name__)
#app.config.from_object(Configuration)
#from module import models
from dl import views
