import tornado.httpserver
import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello World')

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8123)
    tornado.ioloop.IOLoop.instance().start()
