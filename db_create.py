from app import db
from models import BlogPost, User

#create the database and the db tables
# db.create_all()

# insert
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("ghooo", "ghooo@ghoo.com", "ghooo"))

db.session.add(BlogPost("Good", "I\'m good.", 1))
db.session.add(BlogPost("Well", "I\'m well.", 1))
db.session.add(BlogPost("postgres", "we setup a local postgres", 2))

# commit the changes
db.session.commit()