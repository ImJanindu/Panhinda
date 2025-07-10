from flask import Flask
from config import Config
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

# Initialize extensions (without app)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()
sess = Session()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)
    sess.init_app(app)

    # Configure login manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Login Required'

    # Import and register blueprints
    from app.auth import bp as auth_bp
    from app.articles import bp as articles_bp
    from app.profile import bp as profile_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(articles_bp)
    app.register_blueprint(profile_bp)

    # Register custom Jinja filter
    from app.utils.func import utc_to_local
    app.jinja_env.filters['utc_to_local'] = utc_to_local

    # Import models (for migrations, etc.)
    from app.auth import models as _  # noqa: F401
    from app.articles import models as _  # noqa: F401

    return app
