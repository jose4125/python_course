# This script demonstrates the use of assertions in Python.
# assertions are used to verify that certain conditions hold true during execution.
# If an assertion fails, an AssertionError is raised with an optional message.
# the program will terminate when an assertion fails.
def divide(a, b):
    assert b != 0, 'Denominator must not be zero'
    print(f'Result of division: {a / b}')

def average_grades(grades):
    assert len(grades) != 0, 'Grades list must not be empty'
    average = sum(grades) / len(grades)
    print(f'Average grade: {average}')

def apply_discount(products, discount):
    price_with_discount = products['price'] * (1.0 - discount)
    print(f'Price after discount: {price_with_discount:.2f}')
    assert 0 <= price_with_discount <= products['price'], f'Discounted price must be between 0 and original price, {price_with_discount:.2f}'
    print ('Discount applied successfully.')

if __name__ == '__main__':
    print('Testing divide function:')
    divide(5,2)
    divide(3,0) # This will raise an assertion error
    print('Testing average_grares function:')
    average_grades([90, 80, 85])
    average_grades([]) # This will raise an assertion error
    print('Testing apply_discount function:')
    product = {'name': 'Laptop', 'price': 1500}
    apply_discount(product, 0.10)
    apply_discount(product, 1.2) # This will raise an assertion error
