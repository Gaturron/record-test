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

# This is just the simplest possible working example that will allow
# you to record to Google Apps Engine and play it back.  It does not
# have session tracking.  It just stores temporary data in a global
# variable.  You can use this to get you started with GAE without
# worrying about data storage.

class wami_handler(webapp2.RequestHandler):
    Ctype = ""
    data = []

    def get(self):
        self.response.headers['Content-Type'] = wami_handler.Ctype
        self.response.out.write(wami_handler.data);
        logging.info("server-to-client: " + str(len(wami_handler.data)) +
                     " bytes of type " + wami_handler.Ctype)

    def post(self):
        wami_handler.Ctype = self.request.headers['Content-Type']
        wami_handler.data = self.request.body
        logging.info("client-to-server: " + str(len(wami_handler.data)) +
                     " bytes of type " + wami_handler.Ctype)
        
# def main():
#     application = webapp.WSGIApplication([('/audio', wami_handler)],
#                                          debug=True)
#     util.run_wsgi_app(application)

# if __name__ == '__main__':
#     main()