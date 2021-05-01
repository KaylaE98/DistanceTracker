#__init__.py file

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# initiates the database SQLAlchemy for later use
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'abc123'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # user_id is the primary key of the user table, so it is used here
        return User.query.get(int(user_id))

    # provides the blueprint for the auth route
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # provides the blueprint for all routes that are not auth
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
