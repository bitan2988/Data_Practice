


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

	def fullName(self):
		return f'{self.frst_name} {self.last_name}'


emp1 = Employee('Yash', 'Sharma', '9999999')
emp1.frst_name = 'Arjun'
print(emp1.email)
print(emp1.fullName())