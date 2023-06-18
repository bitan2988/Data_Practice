
# In programming language design, a first-class citizen (also type, object, entity, or value) in a given programming language is an entity 
# which supports all the operations generally available to other entities. These operations typically include being passed as an argument, 
# returned from a function, and assigned to a variable.[1]

# Higher-Order function : When a function accepts a function as an argument or returns a function


def square(x):
	return x*x

func1 = square  # now we can use this variable func1 as a function
val1 = square(5)

print(func1)
print(val1, func1(4))


def higherOrder1(func, arr):
	for i in range(len(arr)):
		val = func(arr[i])
		arr[i] = val

	return arr

arr = [i for i in range(11)]
ans = higherOrder1(square, arr)
print(ans)



def tagger(tag):

	def message(msg):
		return f'<{tag}>{msg}</{tag}>'

	return message

htmlHeader = tagger('h1')
htmlMsg = htmlHeader('This is a header')
print(htmlMsg)

