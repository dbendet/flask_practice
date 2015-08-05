from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)

class NytArticle(db.Model):
    # __tablename__ = 'nyt_articles'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(128))
    rank = db.Column(db.Integer)
    title = db.Column(db.String(512))
    desc = db.Column(db.String(512))
    thumb = db.Column(db.String(256))
    link = db.Column(db.String(256))
    fetch_date = db.Column(db.DateTime)
    day_id = db.Column(db.Date, index=True)


    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'rank': self.rank,
            'title': self.title,
            'desc': self.desc,
            'thumb': self.thumb,
            'link': self.link,
        }


    def __repr__(self):
        return '<NYT %r>' % self.id