import cgi
import datetime
import urllib
import webapp2

import jinja2
import os

import json

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../view/wami')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(filename))

class basic(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('basic.html')
        self.response.out.write(template.render())

    def post(self):

        Ctype = self.request.headers['Content-Type']
        data = self.request.body
        logging.info("client-to-server: " + str(len(data)) +
                     " bytes of type " + Ctype);

        audio = User(date=datetime.now(), audio=data)
        audio.put()

        self.redirect('/basic')