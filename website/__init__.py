# makes the website folder a python package 
# we can import this folder and as soon as we import it
# it will run automatically whatever is in __init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'
    app.config['secret_key'] = 'secretkeyy'
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app