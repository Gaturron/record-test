import cgi
import datetime
import urllib
import webapp2

import jinja2
import os

import json

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../view/record')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(filename))

class record(webapp2.RequestHandler):

    def get(self):
        template = jinja_environment.get_template('record.html')
        self.response.out.write(template.render())