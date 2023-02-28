"""
TEMPLATES
"""

import flask as fl
import json

app = fl.Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    print(json.dumps(fl.request.args))
    return fl.render_template(
        "index7.html",
        x=int(fl.request.args['x']),
        y=int(fl.request.args['y']),
        query = fl.request.args.to_dict())

if __name__ == "__main__":
    app.run()