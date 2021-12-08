def decorator_function(original_func):
	def wrapper_function():
		print('hello world!')
		return original_func()
	return wrapper_function

@decorator_function
def disp():
	print('This disp func ran!')

def display_info

# decorated_disp = decorator_function(disp)
# decorated_disp()

disp()

# hi_func = outer_func('Hi')

# hi_func()