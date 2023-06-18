# https://www.analyticsvidhya.com/blog/2021/07/python-most-powerful-functions-map-filter-and-reduce-in-5-minutes/

import functools as ft


nums = [i for i in range(11)]
print('nums = ',nums)

letters = [chr(ord('a')+n) for n in range(26)]
print('letters = ',letters)

# using map+lambda
square_nums_map = list(map(lambda n:n*n, nums))
print(square_nums_map)

square_nums = [n*n for n in nums]
print(square_nums)


# Filter only returns value which return a True for the provided condition
even_nums_filter = list(filter(lambda n: n%2 == 0, nums))
print(even_nums_filter)

even_nums = [n for n in nums if n%2 == 0]
print(even_nums)


# Reduce
sum_nums = ft.reduce(lambda a, b: a+b, nums)   
print(sum_nums)


# 2 for loops in list_comprehension	
letter_num_pair = [(letter, num) for letter in letters for num in nums]
print(letter_num_pair[:5])



# Zip
print('zip = ', list(zip(nums, letters)))

# dictionary comprehension
my_dict = {num: letter for num, letter in zip(nums, letters)}
print(my_dict)

my_dict_except = {num: letter for num, letter in zip(nums, letters) if num != 0}
print(my_dict_except)


# Set comprehension
my_set = {n for n in nums}
print(type(my_set)) 


# Generator comprehension
my_generator = (n*n for n in nums)
print(type(my_generator))

