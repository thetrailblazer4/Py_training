def decorator_function(original_func):
	def wrapper_function(*args, **kwargs):
		print('hello world!')
		return original_func(*args, **kwargs)
	return wrapper_function

@decorator_function
def disp():
	print('This disp func ran!')

@decorator_function
def display_info(name, age):
	print(f"display_info ran with args: '{name}' '{age}'")

display_info('John', 26)
