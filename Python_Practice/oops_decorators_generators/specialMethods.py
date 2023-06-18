# 


class Employee:

	def __init__(self, fname, lname, pay):
		self.frstName = fname
		self.lastName = lname
		self.pay = pay
		self.fullName = self.frstName + ' ' + self.lastName
		self.email = self.frstName + '.' + self.lastName + '@bcompany.com'

	def __repr__(self):
	# this function should be used more by the testing team or for logging
	# mention some sort of code which can be used to re-create that instance
	# it will be now dislpayed whwnever we put a print(instance_name)	
		return f'Employee({self.frstName}, {self.lastName}, {self.pay})'

	def __str__(self):
	# More readable for end user
		return f'{self.fullName}, {self.email}'

	def __add__(self, other):  # will over-ride the + operator
		return self.pay + other.pay


if __name__ == '__main__':
	emp1 = Employee('test', 'user1', 100)
	print(emp1) # run this print statement by commenting __repr__ and then commenting __str__ and then commenting both

	#print(repr(emp1))
	#print(str(emp1))

	emp2 = Employee('test', 'user2', 100)

	print(emp1 + emp2)