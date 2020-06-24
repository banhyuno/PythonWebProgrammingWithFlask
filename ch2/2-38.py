from flask import request, Flask

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("answer", 1, type=int)

app.debug = True
app.run()