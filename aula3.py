"""
URL DINÂMICA
"""

import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def index():
    return "<h1 align='center'>INDEX</h1>"

@app.route("/hello/")
@app.route("/hello/<name>/")
@app.route("/hello/<name>/<int:age>/")
def hello(name:str = "", age:int=-1):
    if age > -1:
        return f"<h2 align='center'>HELLO {name}, {age}</h2>"
    elif name != "":
        return f"<h2 align='center'>HELLO {name}</h2>"
    else:
        return "<h2 align='center'>HELLO</h2>"

if __name__ == "__main__":
    app.run(debug=True)