"""
UPLOAD DE ARQUIVOS
"""

import flask as fl
import werkzeug
import os

app = fl.Flask(__name__, template_folder='templates', static_folder='static')
UPLOAD_FOLDER = os.path.join(os.getcwd(), "static/upload")

@app.route("/")
def index():
    return fl.render_template("index11.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    file = fl.request.files['image']
    save_path = os.path.join(
        UPLOAD_FOLDER,
        werkzeug.utils.secure_filename(filename=file.filename)
    )
    file.save(save_path)
    sucess = True
    print(save_path)
    return fl.render_template("index11_upload.html", sucess=sucess, save_path=save_path)

@app.route("/getFile/<filename>")
def getFile(filename:str):
    file = os.path.join(
        UPLOAD_FOLDER,
        werkzeug.utils.secure_filename(filename=filename+".png")
    )
    print(file)
    return fl.send_file(file, mimetype="image/png")

if __name__ == "__main__":
    app.run()