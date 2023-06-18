# Inheritance 
# Method Resolution Order


class Employee:

	raise_amnt = 1.04

	def __init__(self, fname, lname, pay):
		self.frstName = fname
		self.lastName = lname
		self.pay = pay
		self.fullname = self.frstName + ' ' + self.lastName

	def apply_raise(self):
		self.pay = self.pay * self.raise_amnt


class developer(Employee):
	raise_amnt = 1.10

	def __init__(self, fname, lname, pay, progLanguage):
		super().__init__(fname, lname, pay)   # we want Employee class to handle the first 3 params as it has in ints contructor (works for single inheritance as only 1 parent class)
		Employee.__init__(self, fname, lname, pay)
		self.programmingLanguage = progLanguage


class manager(Employee):

	def __init__(self, fname, lname, pay, employees = None):
		Employee.__init__(self, fname, lname, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('--> ', emp.fullname, end = '\n')



if __name__ == '__main__':
	emp1 = Employee('Yash', 'Sharma', 100000)
	emp1.apply_raise()
	print(emp1.pay)


	dev1 = developer('Bitan', 'Sarkar', 100000, 'Python')
	dev1.apply_raise()
	print(dev1.pay)

	dev2 = developer('Arjun', 'Anand', 150, 'Java')

	manager1 = manager('Saikat', 'Bishal', 200, [dev1, dev2])
	manager1.print_emps()

	print(isinstance(manager1, manager))
	print(issubclass(developer, Employee))


	# print(help(developer))
	# print(help(Employee))