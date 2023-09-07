import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        data_array = [
            {"Name": "John", "Age": 25},
            {"Name": "Jane", "Age": 30},
            {"Name": "Bob", "Age": 28}
        ]
        self.render("index.html", data_array=data_array)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
  
