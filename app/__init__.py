from flask import Flask
from dotenv import load_dotenv, get_key
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)

def env_load_dir(env_key, default, config_key = None):
    directory = os.getenv(env_key, default)
    if not config_key is None:
        app.config[config_key] = directory
    if not os.path.isdir(directory):
        os.makedirs(directory)

env_load_dir('UPLOAD_DIR', 'data/archieves', 'UPLOAD_DIR')
env_load_dir('TMP_DIR', 'data/tmp', 'TMP_DIR')
env_load_dir('VID_DIR', 'data/renders', 'VID_DIR')
