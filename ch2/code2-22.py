from flask import Flask

app = Flask(__name__)

# @app.route("/flask")
# def index():
#     return ""

# @app.route("/board/<article_id>")
# @app.route("/board", defaults={"article_id": 10})
# @app.route("/board", methods=["GET","POST"])
# @app.route("/board", subdomain="test")
# def index():
#     # return "{}번 게시물을 보고 계십니다.".format(article_id)
#     return "/board url을 호출하셨습니다."
# # app.add_url_rule("/", "index", index)

@app.route("/board", redirect_to="/new_board")
def board():
    return "/board URL을 호출하셨는데 실행이 안될겁니다"
    
@app.route("/new_board")
def new_board():
    return "/new_board URL이 호출되었습니다."

if __name__ == "__main__":
    app.debug = True
    app.run()