from flask import Blueprint, render_template, request
import functions

main_blueprint = Blueprint('main_blueprint', __name__)
search_blueprint = Blueprint('search_blueprint', __name__)

@main_blueprint.route('/')
def profile_page():
    return render_template("index.html")


@search_blueprint.route('/search/')
def search_page():
    s = request.args['s']
    search_post = functions.search_post(s)

    if search_post != "Пост не найден":
        return render_template("post_list.html", search=s, posts=search_post)
    else:
        return "Пост не найден"