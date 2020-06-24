from flask import Flask, request

app = Flask(__name__)

@app.route("/board", methods=["GET", "POST"])
def board_list():
    # arg_answer = request.args.get('question')
    article_id = request.args.get("article", "1", int)
    # return "answer : " + arg_answer
    # return str(article_id)
    return request.values.get("question", 1, type=int)

app.debug = True
app.run()