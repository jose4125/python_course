class Dog:
    species = "Canis familiaris"  # Class variable
    legs = 4  # Protected class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

layla = Dog('Layla', 5)
buddy = Dog('Buddy', 3)

# Accessing instance variables
print(f'layna: {layla.name} - age: {layla.age}')
print(f'layna: {buddy.name} - age: {buddy.age}')

# Accessing class variable
print(f'layla is a {layla.species}')
print(f'buddy is a {buddy.species}')

print(f'layla has {layla.legs} legs')
print(f'buddy has {buddy.legs} legs')
print(f'class has {Dog.legs} legs')

# Modifying class variable only for layla instance
layla.legs = 6 # This creates an instance variable 'legs' for layla and shadows the class variable
print(f'layla has {layla.legs} legs')
print(f'layla class variable has {layla.__class__.legs}')
print(f'buddy has {buddy.legs} legs')
print(f'class has {Dog.legs} legs')

# Creating a new class variable
Dog.tail = 1
print(f'layla has {layla.tail} tail')
print(f'buddy has {buddy.tail} tail')
print(f'class has {Dog.tail} tail')

# Creating name class variable
# instance variable name shadows the class variable name
Dog.name = 'Dog Class'
print(f'layla name is {layla.name}')
print(f'buddy name is {buddy.name}')
print(f'class name is {Dog.name}')
