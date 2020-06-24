from flask import request, Flask

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("question", "질문을 입력하십시오")

app.debug = True
app.run()