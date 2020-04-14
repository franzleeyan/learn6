## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __int__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __int__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __int__(self, name):
        ## ??
        self.name = name

    ## Person has-a pet of some kind
    self.pet = None

## ??
class Employee(Person):

    def __int__(self, name, salary):
        ## ??
        super(Employee, self).__int__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()