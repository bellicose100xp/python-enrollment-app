from  flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__) #identify the current application being rendered
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

#import it after the app so as not to cause circular dependency with routes.py as it imports app in its dependencies
from application import routes

