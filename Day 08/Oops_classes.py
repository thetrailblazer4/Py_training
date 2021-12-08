# Class and instances

'''
Classes allow us to logically group the data and functions in a way which is easy to reuse
'''


class Emp:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

	def fullname(self):
		return f"{self.first} {self.last}"


emp_1 = Emp('John', 'K', 50000)
emp_2 = Emp('Jane', 'M', 60000)



# print(f"{emp_1.first} {emp_1.last}")
# print(f"{emp_2.first} {emp_2.last}")

print(emp_2.fullname())
print(Emp.fullname(emp_1))
