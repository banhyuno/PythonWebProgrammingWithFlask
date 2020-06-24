from flask import request, Flask

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("question")

app.debug = True
app.run()