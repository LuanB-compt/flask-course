"""
REDIRECIONAMENTO E ERROS
"""

import flask as fl
import json

app = fl.Flask(__name__)

@app.route("/")
def index():
    return fl.render_template(template_name_or_list="index5.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if fl.request.method == "POST":
        if fl.request.form['user'] == "admin" and fl.request.form['password'] == "admin":
            return fl.redirect(location=fl.url_for(endpoint="sucess"), code=302) #200 or 302
        else:
            fl.abort(401)
    else:
        fl.abort(403)

@app.route("/loged")
def sucess():
    return fl.render_template(template_name_or_list="index.html")

if __name__ == "__main__":
    app.run()