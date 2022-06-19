from flask import Flask, request, render_template, send_from_directory
# from functions import ...

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

from main.main import main_blueprint
from main.main import search_blueprint
from loader.loader import load_blueprint
from loader.loader import load_post_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(load_blueprint)
app.register_blueprint(load_post_blueprint)


app.run()

