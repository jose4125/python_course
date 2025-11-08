from logger import log

class Person:
    def __init__(self, person_id: int = None, name: str = None, last_name: str = None, email: str = None):
        self.__person_id = person_id
        self.__name = name
        self.__last_name = last_name
        self.__email = email

    @property
    def person_id(self):
        return self.__person_id

    @person_id.setter
    def person_id(self, person_id: int):
        self.__person_id = person_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    def __str__(self):
        return f'{self.__person_id} - {self.name} {self.last_name} {self.email}'

if __name__ == '__main__':
    person1 = Person(1, 'John', 'Doe', 'johndoe@gmail.com')
    log.debug(person1)
    person2 = Person(name ='Jane', last_name ='Doe', email ='janedoe@gmail.com')
    log.debug(person2)
    person3 = Person(person_id = 4)
    log.debug(person3)