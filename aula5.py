"""
ARQUIVOS ESTÁTICOS
"""

import flask as fl

app = fl.Flask(__name__, static_folder='static')

if __name__ == "__main__":
    app.run(debug=True)