def test_decorator(fn):
    def wrapper(*args, **kwargs):
        print('code before calling the greeting function')
        result = fn(*args, **kwargs)
        print('code after calling the greeting function')
        return result

    return wrapper

@test_decorator
def greeting(name):
    print(f'hola {name}')


greeting('john')