"""
MÉTODOS HTTP
"""

import flask as fl
import json

app = fl.Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return fl.render_template(template_name_or_list="index5.html")

@app.route("/add", methods=["GET", "POST"])
def add():
    if fl.request.method == "POST":
        return json.dumps(fl.request.form)
    elif fl.request.method == "GET":
        return "get method"

if __name__ == "__main__":
    app.run(debug=True)