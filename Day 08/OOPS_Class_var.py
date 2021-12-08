# Class Variable


class Emp:

	raise_amt = 1.04
	nums_of_emp = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = int(pay)
		self.email = f"{first}.{last}@company.com"

		Emp.nums_of_emp += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


print(Emp.nums_of_emp)

emp_1 = Emp('John', 'K', '50000')
emp_2 = Emp('Jane', 'M', 60000)
print(Emp.nums_of_emp)

emp_2.raise_amt = 1.05

# print(Emp.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)