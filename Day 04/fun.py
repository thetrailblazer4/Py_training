# def hello_fun():
# 	print('hello!')

# hello_fun()
# hello_fun()
# hello_fun()
# hello_fun()
# hello_fun()
# hello_fun()
# hello_fun()

# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')
# # print('Hello!')



# print(list(range(10)))


# for i in range(5):
# 	print('hello')


# def hello_fun(message, name='You'):
# 	return f"{message} {name}"

# print(hello_fun('Hello', 'John'))


def emp_info(*args, **kwargs):
	print(args)
	print(kwargs)

emp_info('Python', 'java', 'JS', name='John', age=26)