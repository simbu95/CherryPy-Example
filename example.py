import cherrypy
import os

class myWebServer(object):
    @cherrypy.expose
    def index(self):
        myHTML = open('index.html', 'r')
        return myHTML.read()

cherrypy.log.screen = None
host = '0.0.0.0'
http_port = 80
cherrypy.server.unsubscribe()

#  Setup the HTTP server that will always run
http_server = cherrypy._cpserver.Server()
http_server.socket_port = http_port
http_server._socket_host = host
http_server.subscribe()
www_cfg = {
    '/': {
        'tools.encode.encoding': 'utf-8',
        'tools.sessions.on': True,
        'tools.staticdir.root': os.path.abspath(os.getcwd())
    },
    '/scripts': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './scripts'
    },
    '/styles': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './styles'
    },
    '/images': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './images'
    },
    '/fonts': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': './fonts'
    }
}
cherrypy.tree.mount(myWebServer(), '/', www_cfg)
print('Web Server is running')
print('Directory where you can include extra scripts.... ' + os.path.abspath(os.getcwd()))
if hasattr(cherrypy.engine, "console_control_handler"):
    cherrypy.engine.console_control_handler.subscribe()

#  Start / run the server
cherrypy.engine.start()
cherrypy.engine.block()