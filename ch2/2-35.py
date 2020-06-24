from flask import request, Flask

app = Flask(__name__)

@app.route("/board", methods=["POST"])
def board():
    article_id = request.form.get("article", "1", int)
    return str(article_id)

app.debug = True
app.run()