
# def lines(func):
#         def wrapper():
#             print("-"*20)
#             func()
#             print("-"*20)
#         return wrapper
        
class Person:
    """
    Person class
    """
    atr = 10
    def __init__(self, name = 'no name', age = 0):
        self._name = name
        self.__age = age
        self.__address = 'n/a'

    def set_address(self, addr):
        self.__address = addr

    def get_address(self):
        return self.__address

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Error!')

    # @lines
    def description(self):
        print("-"*20)
        print(f"| My name is {self._name}")
        print(f"| I am {self.__age}")
        print(f"| I live in {self.__address}")
        print("-"*20)

if __name__ == '__main__':
    person_1 = Person('Bob', 30)
    person_1.description()