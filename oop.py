# абстракція
# наслідування
# інкапсуляція
# поліморфізм

#                   фігура
#                   побудова():pass
#                   line_color
#                   line_type
#                   fill

# коло          квадрат     трикутник
# побудова()    побудова()  побудова()

# incapsulation
# _ - protected
# __ - private

class Person:
    atr = 10
    def __init__(self, name = 'no name', age = 0):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('Error!')

    def description(self):
        print(f'My name is {self._name}\nI am {self.__age}')


person_1 = Person('Bob', 30)
# person_1.set_age(31)
# print(person_1.get_age())
person_1.age = -1
print(person_1.age)
# person_1.description()
# person_1.atr = 200
# print(person_1.name, person_1.age, person_1.atr)

# person_2 = Person('Bil', 40)
# person_2.description()
# print(person_2.name, person_2.age, person_2.atr)