import tornado.ioloop
import tornado.web
import tornado.websocket
import os


# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write('hello, Torando')

# def make_app():
#     return tornado.web.Application([
#         (r'/', MainHandler)
#     ])

# if __name__ == '__main__':
#     app = make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # response = ','.join(WebSocketHandler.cache)
        # self.write(response)
        self.render("index.html", messages=WebSocketHandler.cache)

class WebSocketHandler(tornado.websocket.WebSocketHandler):
    waiters = set()
    cache = []
    def open(self):
        WebSocketHandler.waiters.add(self)
    def on_close(self):
        WebSocketHandler.waiters.remove(self)
    @classmethod
    def update_cache(cls, message):
        cls.cache.append(message)
    @classmethod
    def send_updates(cls, news):
        print(len(cls.waiters))
        for waiter in cls.waiters:
            try:
                waiter.write_message(news)
            except:
                print('Error sending message')

    def on_message(self, message):
        self.write_message(u'Your message was: ' + message)
        WebSocketHandler.update_cache(message)
        WebSocketHandler.send_updates(message)
        print(WebSocketHandler.cache)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/websocket',WebSocketHandler),
            (r'/',MainHandler),
        ]
        settings = dict(
            cookie_secret="SADOIFANW3ROI32IR33JQFEJENF23OI23KN2RN23RK2RKOO",
            static_path=os.path.join(os.path.dirname(__file__), "./"),
            xsrf_cookies=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    app = Application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()