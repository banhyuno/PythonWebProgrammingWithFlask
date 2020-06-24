from flask import request, Flask

app = Flask(__name__)

@app.route("/board")
def board():
    article_id = request.args.get("article", "1", int)
    return str(article_id)

app.debug = True
app.run()