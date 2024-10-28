def check_division(func):
    def wrapper(*args):
        if args[1] == 0:
            return"Деление на ноль невозможно"
        else:
            result = func(*args)
            return result
    return wrapper

@check_division
def divide(a, b):
    return a / b
print(divide(10, 0))