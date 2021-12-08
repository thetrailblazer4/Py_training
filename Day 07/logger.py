import logging

logging.basicConfig(filename='logger.log', level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info(f"Running '{func.__name__}' with args {args} ")
		print(func(*args))
	return log_func


def add(x,y):
	return x + y

def sub(x,y):
	return x - y

add_logger = logger(sub)
add_logger(5,4)

# print(add(6,2))