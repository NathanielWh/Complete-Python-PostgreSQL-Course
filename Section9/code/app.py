from database import Database
from user import User

Database.initialise(database="learning", host="localhost", user="postgres", password="muffin")

my_user = User('anne@smith.com', 'Rolf', 'Smith', None)

my_user.save_to_db()

user_from_db = User.load_from_db_by_email('jose@schoolofcode.me')

print(user_from_db)

