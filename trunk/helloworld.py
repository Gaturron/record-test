import cgi
import datetime
import urllib
import webapp2

import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import db
from google.appengine.api import users

from controller.callback import callback
from controller.wav import wav
from controller.write import write
from controller.mic import mic
from controller.record import record

from controller.record_mic import record_mic
from controller.basic import basic

from controller.wami_handler import wami_handler
from controller.audios import audios

app = webapp2.WSGIApplication([('/callback', callback),
                               ('/wav', wav),
                               ('/write', write),

                               ('/mic', mic),
                               ('/record', record),
                               ('/record_mic', record_mic),

                               ('/basic_mic', basic),

                               ('/wamihandler', wami_handler),
                               ('/audios', audios)
                              ],
                              debug=True)
