from google.appengine.ext import db

class Audio(db.Model):
  date = db.DateTimeProperty(auto_now=True)
  audio = db.BlobProperty()