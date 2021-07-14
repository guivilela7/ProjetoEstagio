from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '71cb9758760815713f04072636f9828b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alunos.db'

database = SQLAlchemy(app)

from sistema_notas import routes
