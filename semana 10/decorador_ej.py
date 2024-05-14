from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Antes de llamar la función")
        result = func(*args, **kwargs)
        print (result.upper())
        print("Despues de llamar la función")
        return result.upper()
    return wrapper

@my_decorator
def greet(name):
    return (f"Hola, {name}")

greet("Juan")

print(greet.__name__)
print(greet.__doc__)