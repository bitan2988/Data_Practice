
# Python first looks for Local variables, then Enclosed variable, then Global variables, then BuiltIns  (LEGB)

x = 'global x'
y = 'global y'

def outer():
	x = 'outer x'
	global y  # mentioning that we want to refer the global y
	y = 'outer y'  # now these changes are made to the global y
	z = 'outer z'

	def inner():
		x = 'inner x'
		nonlocal z # referencing the z inside the enclosing
		z = 'inner z'  # changes made to the enclosed variable

		print(x)
		print(y) # y is the enclosed variable i.e variable of the outer function
	inner()

	print(x)
	print(y)
	print(z)


outer()
print(x)
print(y)
