# special methods


class Emp:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = f"{first}.{last}@company.com"

	def fullname(self):
		return f"{self.first} {self.last}"

	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}', '{self.pay}')"

	def __str__(self):
		return f"{self.fullname()} - {self.email}"


emp_1 = Emp('John', 'K', 50000)
emp_2 = Emp('Jane', 'M', 60000)

print(emp_1)

print(emp_1.__repr__())
print(emp_1.__str__())

print(repr(emp_1))
print(str(emp_1))

# print(emp_2.fullname())
# print(Emp.fullname(emp_1))
