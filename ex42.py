## Animal is-a object 
class Animal(object):
	pass

##Dog is-a Object
class Dog(Animal):

	def __init__(self, name):
		##an instance of Dog has-a name
		self.name = name

##Cat is an Object
class Cat(Animal):

	def __init__(self, name):
		##an instance of Cat has-a name
		self.name = name

##Person is-an Object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

##Employee is-an object
class Employee(Person):

	def __init__(self, name, salary):
		##Employee has-a name
		super(Employee, self).__init__(name)
		##Employeee has-a salary
		self.salary = salary

##Fish is-an object
class Fish(object):
	pass

##same as above
class Salmon(Fish):
	pass

##object
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

##mary's pet is satan
mary.pet = satan

##frank is an Employee with a salary of 120k
frank = Employee("Frank", 120000)

##frank's pet is rover
frank.pet = rover

##flipper is-a fish
flipper = Fish()

##course is-a salmon, which is-a fish, which is-an object
crouse = Salmon()

##harry is-a halibut, which is-a fish, which is-an object
harry = Halibut()