import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Flask security params
    SECRET_KEY = os.environ.get("SECRET_KEY")
    
    # Flask SQLAlchemy params
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or f"sqlite:///{os.path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") == "True"
    
    # Flask session params
    SESSION_PERMANENT = os.environ.get("SESSION_PERMANENT") == "True"
    SESSION_TYPE = os.environ.get("SESSION_TYPE") or "filesystem"
        
    # Flask mail params
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 465))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") == "True"
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL") == "True"

    # Flask paths
    USER_DATA_PATH = os.environ.get("USER_DATA_PATH") or os.path.join(basedir, "static", "user_data")
