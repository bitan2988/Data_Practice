
nums = [i for i in range(11)]
print(nums)

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
