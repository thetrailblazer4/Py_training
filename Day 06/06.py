# LEGB -- Local --> Enclosing --> Global --> Builtins

# x = 'Global x'


# def demo_func(z):
# 	x = 'local x'
# 	print(z)


# demo_func('hello')
# print(x)



# nums = [4,1,3,2,5]


# def max():
# 	pass

# def max(x):
# 	pass

# m = max(nums)
# print(m)


# import builtins

# print(dir(builtins))


x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)
	inner()

	print(x)

outer()
print(x)