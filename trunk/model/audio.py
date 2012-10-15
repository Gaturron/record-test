from google.appengine.ext import db

class Audio(db.Model):
  date = db.DateProperty()
  audio = db.BlobProperty()