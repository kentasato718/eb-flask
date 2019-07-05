from flask import Flask

application = Flask(__name__, static_url_path='/app/static')
application.config['SECRET_KEY'] = '$ECrEt'
from app import routes  # avoid circular imports
