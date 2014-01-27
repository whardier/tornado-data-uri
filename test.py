import tornado.ioloop
import tornado.web
import tornado.template

import tornado_data_uri.uimodules

class UIModuleTestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.ui.html')

application = tornado.web.Application(
    [
        (r"/uimodule", UIModuleTestHandler),
    ],
    ui_modules={'static_file_data_uri_base64': tornado_data_uri.uimodules.static_file_data_uri_base64},
    static_path='./static',
    template_path='./template',
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
