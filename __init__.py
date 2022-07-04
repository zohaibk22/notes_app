from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DB_NAME= 'database.db'

def create_app():
    app = Flask(__name__)

    # __name__ just represents the file that will be ran....also initialized flask
    app.config['SECRET_KEY'] = 'NDNFNDJN FJNVJND SNVJSND'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # ^^ Encrypts and secures our session data and cookies related to our website
    #  We can type in a random string, which will be our secret key for our app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
