"""
ENVIANDO DADOS PARA TEMPLATES
"""

import flask as fl

app = fl.Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return fl.render_template(template_name_or_list="index8.html")

@app.route("/result", methods=["POST"])
def result():
    results, sum = fl.request.form.to_dict(), 0
    print(results)
    for score in results:
        if score == "score0":
            sum+=(float(results[score]) * 0.15)
        elif score == "score1":
            sum+=(float(results[score]) * 0.3)
        elif score == "score2":
            sum+=(float(results[score]) * 0.1)
        elif score == "score3":
            sum+=(float(results[score]) * 0.45)
        else:
            print("aqui")
            fl.abort(404)
    return fl.render_template(template_name_or_list="index8_result.html", sum=sum)

if __name__ == "__main__":
    app.run()