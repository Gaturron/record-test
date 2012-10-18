import cgi
import datetime
import urllib
import webapp2

import jinja2
import os
import logging

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../view/wami')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(filename))

from model.Audio import Audio

class audios(webapp2.RequestHandler):
    def get(self):
        
        audios_query = Audio.all()
        audios = audios_query.fetch(30)

        # mandar la gente por parametro de la pagina
        template_values = {
        	'audios': audios,
        }

        template = jinja_environment.get_template('list.html')
        self.response.out.write(template.render(template_values))