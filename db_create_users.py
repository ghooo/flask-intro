from app import db
from models import BlogPost, User

# insert
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("ghooo", "ghooo@ghoo.com", "ghooo"))

# commit the changes
db.session.commit()