# Allows us to write a method which can be accessed like an attribute

class Employee:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, fname, lname, pay):
		self.frst_name = fname
		self.last_name = lname
		self.pay = pay
		# self.email = fname + '.' + lname + '@lntinfotech.com'    # emp1.email is an attribute and not a method

		Employee.num_of_emps +=1

	@property     # making it a decorator (getter)    
	def email(self):
		return f'{self.frst_name}.{self.last_name}@lntinfotech.com'

	@property  # getter
	def fullName(self):
		return f'{self.frst_name} {self.last_name}'

	# setter name should be the attribute/method followed by a .setter
	@fullName.setter    # we want that whenever we pass the fullName we should be able to change the frstName and the lastName
	def fullName(self, name):
		self.frst_name, self.last_name = name.split(' ')

	@fullName.deleter    # we want that whenever we pass the fullName 
	def fullName(self):
		print('Delete Name!')
		self.frst_name = None
		self.last_name = None

	def pay_range(self):
		print('Hello pay_range')

	def pay_raise(self):
		self.pay = self.pay * self.pay_raise




emp1 = Employee('Yash', 'Sharma', '9999999')

# calling getter
emp1.frst_name = 'Arjun'
print(emp1.email)  # it will still have frst_name as Yash as constructor call is not made (if we uncomment line 12) 
print(emp1.fullName)

# calling setter to reset or frst and lastName as per the new fullName
emp1.fullName = 'Bitan Sarkar'
print(emp1.email)

# calling deleter
del emp1.fullName
print(emp1.email)