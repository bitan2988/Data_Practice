# Generator : A generator function creates a generator object which is not held in the memory,
# 			  It can be accessed by calling the next Method or using the for_in loop

def squaring(nums):
	res = []
	for num in nums:
		res.append(num*num)
	return res

my_nums1 = squaring([1, 2, 3, 4, 5])
print(my_nums1)


# To make the above function a generator
def squaring_generator(nums):
	for num in nums:
		yield (num*num)

my_nums2 = squaring_generator([1, 2, 3, 4, 5])
print('my_nums2 = ',my_nums2
print('next = ',next(my_nums2)) # next calls the next method
print('next = ',next(my_nums2))
print('next = ',next(my_nums2))
print('next = ',next(my_nums2))
print('next = ',next(my_nums2))
# print('Stop Iteration = ',next(my_nums2))  # will throw an error as all the values of the generator_object has been traversed
for num in my_nums2:
	print(num)


# List Comprehension
my_nums3 = [x*x for x in [1, 2, 3, 4, 5]]
print('Normal list comprehension', my_nums3)


# List Comprehension Genrator
my_nums4 = (x*x for x in [1, 2, 3, 4, 5])
print('List comprehension generator : ', my_nums4)


# Converting generator_object into list
my_nums5 = list(my_nums4)
print(my_nums5)


