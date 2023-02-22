"""
CONSTRUÇÃO DE URL
"""

import flask as fl

app = fl.Flask(__name__)

@app.route("/")
def index():
    return fl.render_template(template_name_or_list="index.html")

@app.route("/admin/")
def admin():
        return "<h2 align='center'>Hello admin</h2>"

@app.route("/guest/<user>")
def guest(user:str):
    return f"<h2 align='center'>Hello {user}</h2>"

@app.route("/login/<user>")
def login(user:str):
    if user == 'admin':
        return fl.redirect(location=fl.url_for('admin'))
    else:
        return fl.redirect(location=fl.url_for('guest', user=user))

@app.route("/google/")
def google():
    return fl.redirect(location="http://google.com")

if __name__ == "__main__":
    app.run(debug=True)