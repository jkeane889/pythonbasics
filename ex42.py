# Animal is-a object (yes, sort of confusing) look at the extra credit
class animal(object):
    pass

# Dog is-a class of Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-an attribute named name
        self.name = name

## Cat is-a class of Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is an object
class Person(object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a class of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super is accessing the class Employee and changing the parent class to equal salary
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat('satan')

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan
mary.pet = satan

# frank is-a Employee and has-a salary of 120,000
frank = Employee("Frank", 120000)

# Frank has-a pet named rover
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a halibut
harry = Halibut()
