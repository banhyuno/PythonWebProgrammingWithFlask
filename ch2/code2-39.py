from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

class dateKoreanType:

    def __init__(self, format):
        self.format = format

    def __call__(self, *args, **kwargs):
        return datetime.strptime(args[0], self.format)

# def dateKoreanType(date_format):
#     def translate(date_str):
#         return datetime.strptime(date_str, date_format)
#     return translate

@app.route("/board", methods=["GET", "POST"])
def board():
    print(request.values.get("date", "2015-02-09", type=dateKoreanType("%Y-%m-%d %h")))
    return "날짜는 콘솔을 확인해보세요"

app.debug = True
app.run()