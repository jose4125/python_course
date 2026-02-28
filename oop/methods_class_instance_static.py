class MyClass:
    def instance_method(self):
        return 'Instance Method called', self

    @classmethod
    def class_method(cls):
        return 'Class Method called', cls

    @staticmethod
    def static_method():
        return 'Static Method called'

# Calling instance method
obj1 = MyClass()
print(obj1.instance_method())

# Calling class method
print(obj1.class_method())

# Calling static method
print(MyClass.class_method())

# Calling instance method from class (requires instance as argument)
print(MyClass.instance_method(obj1))

# Calling class method from class
print(MyClass.class_method())