from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template( 
                            "index.tpl", 
                            # "board.tpl", 
                            data1="data1", 
                            data2="data2", 
                            users=( {'username':'TEST',     'url':'http://www.test.com'} 
                                ,   {'username':'TEST2',    'url':'http://www.test2.com'}
                                ,   {'username':'TEST3',    'url':'http://www.test3.com'}
                            ), 
                            seq=(10, 20, 30, 40, 50)
                            )

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.debug = True
app.run()