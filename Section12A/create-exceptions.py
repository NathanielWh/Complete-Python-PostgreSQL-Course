class MissingLabelError(KeyError):
    pass

class PageNotFoundError(ValueError):
    pass

def login():
    raise IncorrectUsernameError

try:
    login()
except IncorrectUsernameError:
    print("Your user name was incorrect.")