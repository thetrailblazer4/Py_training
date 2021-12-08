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

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = str_emp_1.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


emp_1 = Emp('John', 'K', '50000')
emp_2 = Emp('Jane', 'M', 60000)

str_emp_1 = 'John-K-50000'
str_emp_2 = 'Jane-M-60000'

new_emp_1 = Emp.from_string(str_emp_1)

# first, last, pay = str_emp_1.split('-')
# new_emp_1 = Emp(first, last, pay)

print(new_emp_1.first)



# print(Emp.raise_amt)
# Emp.set_raise_amt(1.08)
# print(Emp.raise_amt)


import datetime

my_date = datetime.date(2021,12,5)

print(my_date)

print(Emp.is_workday(my_date))

# print(datetime.__file__)