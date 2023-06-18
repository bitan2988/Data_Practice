
# Regular methods in class by default takes the instance as the first argument
# ClassMethods pass the class_name as the first argument by default
# StaticMethods don't pass anything by default
# We can create class method by using a decorator above @classmethod



class employee:
	raise_amount = 1.04

	def __init__(self, frst_name, last_name, pay):
		self.pay = pay
		self.fname = frst_name
		self.lname = last_name
		self.email = self.fname + '.' + self.lname + '@comp.com'
 
	@classmethod    # now we will receive the class as the first argument
	def raise_amnt(cls, amnt):
		cls.raise_amount = amnt 

	@classmethod  # classMethods can also be used to create alternate constructors for our class (general convention of starting them using 'from_')
	def from_string(cls, emp_str):
		fname, lname, pay = emp_str.split('-')
		return cls.(fname, lname, pay)   # call the original-constructor and return the object

	@staticmethod  # for functions which have a logical connection but might be common for all the instances 
				   # and we dont access the instance or the class even once inside it
	def is_workday(day):
		return True


emp1 = employee()
print(employee.raise_amount)
print(emp1.raise_amount)

employee.raise_amnt(1.05) # accessing the classMethod
emp1.raise_amnt(1.05)  # we can access a classMethod from an instance too

print(employee.raise_amount)
print(emp1.raise_amount)


emp1_str = 'bitan-sarkar-9999'
new_emp1 = employee.from_string(emp1_str)

print(employee.is_workday(today))