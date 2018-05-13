

def divide_secure(number, divisor):
    assert divisor != 0, "Don't divide by zero asshole"
    return number / divisor


print(divide_secure(10, 0))
