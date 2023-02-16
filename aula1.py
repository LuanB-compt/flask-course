"""
ESTRUTURA BÁSICA
"""

import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def index():
    return "<h1 align='center'>INDEX</h1>"

if __name__ == "__main__":
    app.run()