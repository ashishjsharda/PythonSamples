from wsgiref.simple_server import make_server
def application(env,start_response):
    start_response("200 OK",[("Content-type", "text/html")])
    return ["Hello WSGIRef ".encode("utf-8")]
server=make_server('localhost',8080,application)
server.serve_forever()
