
from user import User

my_user = User("jose@schoolofcode.me", "Jose", "Salvatierra", None)

print(my_user.email)

# User __repr__ method to print contents when class is called

print(my_user)

my_user.save_to_db()

