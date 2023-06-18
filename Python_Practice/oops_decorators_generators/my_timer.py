# To detetch which function took how much time to run


def my_timer(original_function):
	import time
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = original_function(*args, **kwargs)
		t2 = time.time() - t1
		print(f'{original_function.__name__} took {t2} seconds to run with the args = {args} and keyWord Arguments = {kwargs.items()}')
		return result
	return wrapper

@my_timer
def func_add(a, b):
	return a+b


if __name__ == '__main__':
	res = func_add(1, 2)
	print(res)