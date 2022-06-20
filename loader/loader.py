from flask import Blueprint, request, render_template
import functions

load_blueprint = Blueprint('load_blueprint', __name__)
load_post_blueprint = Blueprint('load_post_blueprint', __name__)


@load_blueprint.route("/post/")
def load_page():
    return render_template("post_form.html")


@load_post_blueprint.route("/upload", methods=["POST"])
def load_page():
    _ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', ""}
    _text = request.form.get("content")
    picture = request.files.get("picture")
    filename = picture.filename
    _extension = filename.split(".")[-1]

    if _extension not in _ALLOWED_EXTENSIONS:
        return f"Тип файлов {_extension} не поддерживается"

    if len(_text) > 0:
        if picture:
            picture.save(f"./uploads/images/{filename}")
            _name_file = f"/uploads/images/{filename}"

            functions.load_post(_name_file, _text)

            return render_template("post_uploaded.html", file=_name_file, text=_text)
        else:
            return "Ошибка загрузки"
    else:
        return "Ошибка загрузки"





