from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Episode(db.Model):
    __tablename__ = 'Episode'

    id = db.Column(db.Integer, primary_key=True)

# add any models you may need. 