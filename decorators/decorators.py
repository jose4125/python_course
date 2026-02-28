import functools


def uppercase(fn):
    def wrapper():
        print('code before calling the greeting function')
        original_result = fn()
        print('code after calling the greeting function')
        modified_result = original_result.upper()
        return modified_result

    return wrapper

@uppercase
def greet():
    return 'Hello, world!'

print(greet())  # Output: 'HELLO, WORLD!'

# Multiple decorators
def strong(fn):
    def wrapper():
        return f'<strong>{fn()}</strong>'

    return wrapper

def emphasis(fn):
    def wrapper():
        return f'<em>{fn()}</em>'

    return wrapper

@strong
@emphasis
def greet_html():
    return 'Hello, Decorators!'

print(greet_html())

# Simple decorator with arguments
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


# Decorator with arguments
def decorator_with_args(fn):
    def wrapper(*args, **kwargs ):
        print('executing this decorator with arguments')
        print('args:', args)
        print('kwargs:', kwargs)
        text_transform = [arg.upper() for arg in args]
        text_transform.append('new arg 1')
        text_transform.append('new arg 2')

        kwargs['value1'] = 'new kwarg 1'
        kwargs['value2'] = 'new kwarg 2'
        result = fn(*text_transform, **kwargs)
        return result

    return wrapper

@decorator_with_args
def greet2(title, name, *args, **kwargs):
    print('title in greet2:', title)
    print('name in greet2:', name)
    print('args in greet2:', args)
    print('kwargs in greet2:', kwargs)
    return f'{title}, {name}'

print(greet2('Doctor', 'Smith'))




print(' decorators with arguments '. center(40, '='))
user_guest = {'username': 'jenn', 'access_level': 'guest'}
user_admin = {'username': 'jose', 'access_level': 'admin'}
user_user = {'username': 'sirius', 'access_level': 'user'}

def secure_admin_password(fn):
    @functools.wraps(fn)
    def wrapper (*args, **kwargs):
        user = args[0]
        user_name = user['username']
        user_access_level = user['access_level']

        if user_access_level == 'admin':
            return fn(*args, **kwargs)

        return f'No admin permissions for user: {user_name}'

    return wrapper


@secure_admin_password
def get_admin_password(user):
    return f'Admin user: {user['username']}, password: admin123'

@secure_admin_password
def get_dashboard_password(user):
    return f'User: {user['username']}, password: user123'

# with no "@functools.wraps(fn)" it prints "wrapper" instead "get_admin_password"
print('func name', get_admin_password.__name__)
print(get_admin_password(user_guest))
print(get_admin_password(user_admin))



# Decorators with parameters
print(' decorators with params '. center(40, '='))
def secure_password(access_level):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper (*args, **kwargs):
            user = args[0]
            user_name = user['username']
            user_access_level = user['access_level']

            if user_access_level == access_level:
                return fn(*args, **kwargs)

            return f'No {access_level} permissions for user: {user_name}'

        return wrapper
    return decorator


@secure_password('admin')
def get_admin_password(user):
    return f'Admin user: {user['username']}, password: admin123'

@secure_password('user')
def get_dashboard_password(user):
    return f'User: {user['username']}, password: user123'
print(' admin '.center(40, '='))
print(get_admin_password(user_guest))
print(get_admin_password(user_admin))
print(get_admin_password(user_user))
print(' dashboard '.center(40, '='))
print(get_dashboard_password(user_guest))
print(get_dashboard_password(user_admin))
print(get_dashboard_password(user_user))
