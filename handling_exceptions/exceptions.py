from handling_exceptions.custom_exception import CustomError

def divide(numerator, denominator):
    try:
        if denominator == 0:
            # message is optional in built-in errors
            raise ZeroDivisionError

        if numerator == 'custom_error':
            raise CustomError('Error - testing a custom error')

        if numerator < 0:
            # message is optional in built-in errors
            raise ArithmeticError('Numerator have to be greater than 0')

        result = numerator / denominator
        print(f'{numerator} / {denominator}: {result}')
    except ZeroDivisionError as e:
        # print the MRO - Method Resolution Order.
        print(f'MRO ZeroDivisionError:  {ZeroDivisionError.mro()}')
        print(f'Error can not divide by 0 - {e}')
        print(f'Error type - {type(e)}')
    except TypeError as e:
        # print the MRO - Method Resolution Order.
        print(f'MRO TypeError:  {TypeError.mro()}')
        print(f'Error arguments have to be numbers')
        print(f'Error type - {type(e)}')
    except Exception as e:
        print(f'general error Exception: {e}')
        print(f'Error type - {type(e)}')
    else:
        print('no exception calls')


divide(10, 2)
print('\n=== ZeroDivisionError ===')
divide(10, 0)
print('\n=== TypeError ===')
divide(10, '5')
print('\n=== ArithmeticError ===')
divide(-1, 5)
print('\n=== CustomError ===')
divide('custom_error', 5)
