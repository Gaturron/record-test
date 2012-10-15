import cgi
import datetime
import urllib
import webapp2

import jinja2
import os

import json

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../view/sink/tests')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(filename))

class callback(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('callback.html')
        self.response.out.write(template.render())