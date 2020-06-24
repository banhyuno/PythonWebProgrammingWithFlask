from flask import Flask

app = Flask(__name__)

@app.route("/board", endpoint="board")
def board():
    return "!"

@app.route("/board/<article_idx>")
def board_view(article_idx):
    return "~" + article_idx

@app.route("/board", defaults={'page':'index'})
@app.route('/board/<page>')
def board_page():
    return "page"

app.debug=True
app.run(host="0.0.0.0")