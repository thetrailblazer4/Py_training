# # decorator --> first class functions ---> closures

# '''
#  when functions in that language are treated like any other variable. 
#  For example, in such a language, 
#  a function can be passed as an argument to other functions, 
#  can be returned by another function and 
#  can be assigned as a value to a variable.
# '''


# def square(x):
# 	return x * x

# def cube(x):
# 	return x * x * x



# # [1,2,3,4] --> [1,4,9,16]


# def my_result(func, my_lst):
# 	res = []

# 	for i in my_lst:
# 		res.append(func(i))
# 	return res

# my_result(square, [1,2,3,4])
# my_result(cube, [1,2,3,4])

# # square([1,2,3,4])

# # result = square(4)

# # result = square

# # print(result(4))


# # def add(x,y):
# # 	return x + y

# # def sub(x,y):
# # 	return x - y

# # print(add(6,2))

# def outer(msg):
# 	def inner():
# 		print(f"output:{msg}")
# 	return inner


# new_var = outer('hello')
# new_var()
# print(new_var.__name__)

# outer('hello')