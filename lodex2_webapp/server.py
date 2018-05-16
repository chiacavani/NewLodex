import tornado.ioloop
import traceback
import tornado.web
import os
from operator import itemgetter
import igraph
from igraph import *
import pprint
import motor
import time
from tornado import gen


exclusion = []

# VISUALIZZA PRIMA PAGINA
class MainHandlerOk(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("LODeX.html")


# VISULIZZA PAGINA GRAPH
class GraphView(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("graph-view.html")

#VISUALIZZA PAGINA QUERY
class QueryView(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("query-panel.html")


if __name__ == "__main__":
    db = motor.MotorClient()
    db2 = motor.MotorClient().lodex
    application = tornado.web.Application(handlers=[
        (r"/lodex2/ok", MainHandlerOk),
        (r"/lodex2/ok/graph-view", GraphView),
        (r"/lodex2/ok/query-panel", QueryView)],
         static_path=os.path.join(os.path.dirname(__file__), "static"), db=db)
    port = 8891
    print('Listening on http://localhost:', port)
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()