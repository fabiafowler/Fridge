from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

=======
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



>>>>>>> development
from application import routes
