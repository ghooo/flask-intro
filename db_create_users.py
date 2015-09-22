from project import db
from project.models import BlogPost, User

# insert
db.session.add(User("admin", "ad@min.com", "admin"))
db.session.add(User("ghooo", "ghooo@ghoo.com", "ghooo"))

# commit the changes
db.session.commit()