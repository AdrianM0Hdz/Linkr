from . import db

class Alias(db.Model):
    __tablename__ = 'aliasses'
    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String(20), nullable=False, unique=True)
    url = db.Column(db.String(), nullable=False, unique=True) 

    def __repr__(self):
        return f'<Alias alias:{alias} url:{url}>'