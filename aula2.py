"""
ROTAS SEM DECORATOR
"""

import flask as fl

app = fl.Flask(__name__)

def index():
    return "<h1 align='center'>INDEX</h1>"

def test():
    return "<h2 align='center'>TESTANDO</h2>"

app.add_url_rule(rule="/", view_func=index)
app.add_url_rule(rule="/test", view_func=test)

if __name__ == "__main__":
    app.run(debug=True, port="3000")