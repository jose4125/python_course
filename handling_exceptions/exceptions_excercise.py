try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError as err:
    print(err)

try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError as err:
    print(err)
finally:
    print('All Done')

def ask():
    while True:
        try:
            integer = int(input('Enter an integer: '))
        except ValueError as err:
            print(err)
            print('An error occurred! Please try again!')
        else:
            print('thank you, you number squared is:', integer ** 2)
            break

ask()