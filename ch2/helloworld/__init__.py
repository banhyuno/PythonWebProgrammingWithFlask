from flask import Flask, Response, make_response

app = Flask(__name__)

# @app.route("/")
# def helloworld():
#     return "Hello World"

@app.route("/")
# def response_test():
# #     custom_response = Response("Custom Response", 200, {
# #         "Program": "Flask Web Application" # response headers 
# #     })

# #     return make_response(custom_response)
#     # return make_response(u"Custom Response") # unicode text
    
#     def application(environ, start_response):
#         response_body = 'The request method was %s' %environ['REQUEST_METHOD']
#         status = '200 OK'

#         response_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body)))]
#         start_response(status, response_headers)

#         res = [response_body.encode("euckr")]
#         print("res :", res)

#         return res

#     return make_response(application)

def custom_response():
    return make_response(('Tuple Custom Response', 'OK', {
        'response_method': 'Tuple Response'
        , 'test':'test'
    }))