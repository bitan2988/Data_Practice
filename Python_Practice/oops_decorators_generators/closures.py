
# Closures : an inner function that remembers and can access all the variables declared in its local scope even after the execution of the 
#            outer function is over

# Free variable : The variable thats not defined inside the inner functions scope


def outer(msg):
	def inner():
		print(msg)
	return inner

hi_func = outer('Hi')
hello_func = outer('Hello')

hi_func()
hello_func()




def logger(func):
	def log_info(*args):
		print(f'Running "{func.__name__}", with {args} arguments')
		print(func(*args))
	return log_info

def func_add(x, y):
	return x+y

def func_sub(x, y):
	return x-y


logger_add = logger(func_add)
logger_add(5, 5)

logger_sub = logger(func_sub)
logger_sub(5, 5)

