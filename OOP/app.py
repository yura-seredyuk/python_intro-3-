from person import Person
from house import House


person1 = Person('Bob', 35)
person2 = Person('Kate', 35)

House1 = House('Street 1')
House1.settle(person1)
House1.settle(person2)

person1.description()
person2.description()


House1.eviction(person2)
person2.description()
House1.show_residents()