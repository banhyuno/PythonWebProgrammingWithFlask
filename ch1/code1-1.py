from wsgiref.simple_server import make_server

def application(environ, start_response):
    response_body = ['%s: %s' %(key, value) for key, value in sorted(environ.items())]
    response_body = '</br>'.join(response_body)

    # status = '404 Not Found'
    # status = '409 Conflict'
    status = '200 OK'

    response_headers = [('Content-Type', 'text/html'), ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    res = [response_body.encode("euckr")]
    print("res :", res)
    return res

def application2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello World\n'


httpd = make_server(
    'localhost'
    , 8051
    , application
    )

httpd.handle_request()
