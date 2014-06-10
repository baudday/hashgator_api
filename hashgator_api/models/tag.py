from hashgator_api import db

class Tag (db.Model):
  id  = db.Column(db.String(150), primary_key=True)
  tag = db.Column(db.String(80), unique=False)

  def __init__(self, id, tag):
    self.id  = id
    self.tag = tag

  def __repr__(self):
    return '<Tag %r>' % self.tag
