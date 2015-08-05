from app import models, db

u = models.User(nickname='davee', email='dbendd@email.com')
db.session.add(u)
db.session.commit()

print models.User.query.get(1)