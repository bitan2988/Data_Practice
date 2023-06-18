
class Employee:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, fname, lname, pay):
		self.frst_name = fname
		self.last_name = lname
		self.pay = pay
		self.email = fname + '.' + lname + '@lntinfotech.com'

		Employee.num_of_emps +=1

	def pay_range(self):
		print('Hello pay_range')

	def pay_raise(self):
		self.pay = self.pay * self.pay_raise


emp1 = Employee('Yash', 'Sharma', '9999999')
print(emp1.email)

Employee.pay_range(emp1)
emp1.pay_range()  # both above and below code works same only in case when we use class name we have to pass the instance name manually

Employee.raise_amt = 1.05 # changes for the whole class and its instances
print(emp1.__dict__)
print(emp1.raise_amt)

emp1.raise_amt = 1.95 # creates a raise_amt in its name_space for that instance
print(emp1.__dict__)  # it first looks into its own namespace before searching it into his class
print(emp1.raise_amt)
