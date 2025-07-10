import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # flask security params
    SECRET_KEY = os.environ.get("SECRET_KEY") if os.environ.get("SECRET_KEY") else 'Rn4T9Z0eHJkVJr5f-nxSWepJUdk'
    
    # flask sqlalchemy params
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") if os.environ.get("DATABASE_URI") else f"sqlite:///{os.path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") if os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") else False
    
    # flask session params
    SESSION_PERMANENT = os.environ.get("SESSION_PERMANENT") if os.environ.get("SESSION_PERMANENT") else False
    SESSION_TYPE = os.environ.get("SESSION_TYPE") if os.environ.get("SESSION_TYPE") else 'filesystem'
        
    # flask main params
    MAIL_SERVER = os.environ.get("MAIL_SERVER") if os.environ.get("MAIL_SERVER") else 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get("MAIL_PORT")) if os.environ.get("MAIL_PORT") else 465
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") if os.environ.get("MAIL_USERNAME") else 'fot.info.panhinda@gmail.com'
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") if os.environ.get("MAIL_PASSWORD") else "siqo vxfm vmjm tyhb"
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") == "True" if os.environ.get("MAIL_USE_TLS") else False
    MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL") == "True" if os.environ.get("MAIL_USE_SSL") else True

    # flask paths
    USER_DATA_PATH = os.environ.get("USER_DATA_PATH") if os.environ.get("USER_DATA_PATH") else os.path.join(basedir, 'static\\user_data')
    