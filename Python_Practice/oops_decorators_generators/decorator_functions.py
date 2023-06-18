
# A decorator is a function that acceps a function as an argument, adds some functionality and return a function
# (*args, **kwargs) allows us to pass any number of arguments so that the same wrapper_func can be used with
#                   different functions which have different number of arguments passed to it (https://www.geeksforgeeks.org/args-kwargs-python/)
# **kwargs(key-word arguments) : allows us to pass keyworded arguments "Hi", first='Geeks', mid='for', last='Geeks')
#          						 all of which can be accessed as key-value pairs from  kwargs.items

# when we stack decorators the below one gets executed first followed by the above one
# in out case decorator at line 44 gets executed first followed by the decorator at line 43
# becuase if we expant it then it would look like : sub_func = decorator_func1( my_timer( sub_func))

from functools import wraps

def my_timer(original_function):
	import time
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = original_function(*args, **kwargs)
		t2 = time.time() - t1
		print(f'{original_function.__name__} took {t2} seconds to run with the args = {args} and keyWord Arguments = {kwargs.items()}')
		return result
	return wrapper

def decorator_func1(original_func):
	def wrapper_func(*args, **kwargs):
		print(f'Wrapper executed before {original_func.__name__}')
		print(f'args = {args}, kwargs = {kwargs.items()}')
		return original_func(*args, **kwargs)
	return wrapper_func

class decorator_class(object):
	def __init__(self, original_func):  # to pass to our function to the class
		self.original_func = original_func

	def __call__(self, *args, **kwargs):   # to mimic our inner_function aka wrapper_function
		print(f'Call method executed before {self.original_func.__name__}')
		print(f'args = {args}, kwargs = {kwargs.items()}')
		return self.original_func(*args, **kwargs)

def add_func():
	print('Inside add_func')

@decorator_func1   # this line means that sub_func = decorator_func1(sub_func) --> sub_func() , thus allowing us to directly all this code with sub_func()
@my_timer  # adding a secind decorator to this function
def sub_func(x, y, *args, **kwargs):
	print(f'Inside sub_func where sub = {x - y}')
	for key, value in kwargs.items():
		print(f'kwarg {key} = {value}')


@decorator_class   # this line means that sub_func = decorator_func1(sub_func) --> sub_func() , thus allowing us to directly all this code with sub_func()
def sub_func2(x, y, *args, **kwargs):
	print(f'Inside sub_func2 with decoratorClass where sub = {x - y}')
	for key, value in kwargs.items():
		print(f'kwarg {key} = {value}')


# When we are stacking one decorator on top of another, we tend to loose the name of the original_function
# as we return the wrapper_functionName, thus it becomes important to somehow preserve the originalFunction names
# Thus for the same we will use the wraps module from functools package, and enclose all our wrapperFunctions
# inside the @wraps decorator  

def my_timer2(original_function):
	import time

	@wraps(original_function)
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = original_function(*args, **kwargs)
		t2 = time.time() - t1
		print(f'{original_function.__name__} took {t2} seconds to run with the args = {args} and keyWord Arguments = {kwargs.items()}')
		return result
	return wrapper

def decorator_func2(original_func):
	@wraps(original_func)
	def wrapper_func(*args, **kwargs):
		print(f'Wrapper executed before {original_func.__name__}')
		print(f'args = {args}, kwargs = {kwargs.items()}')
		return original_func(*args, **kwargs)
	return wrapper_func

@decorator_func2
@my_timer2  
def sub_func3(x, y, *args, **kwargs):
	print(f'Inside sub_func3 with wraps where sub = {x - y}')
	for key, value in kwargs.items():
		print(f'kwarg {key} = {value}')

if __name__ == '__main__':
	print('--------------------------------------------------------------------------------------------------------')
	dec1 = decorator_func1(add_func)
	print(dec1.__name__)
	dec1()
	print('---------------------------------stacked decorator (without wraps)---------------------------------------')
	sub_func(1, 2, 3, 6, first=4, second=5)  # after adding @decorator_func1 on top of sub_func
	print('---------------------------------with wraps----------------------------------------')
	sub_func3(1, 2, 3, 6, first=4, second=5)
	print('---------------------------------decorator class----------------------------------------')
	sub_func2(1, 2, 3, 6, first=4, second=5)  # after adding @decorator_class on top of sub_func













	