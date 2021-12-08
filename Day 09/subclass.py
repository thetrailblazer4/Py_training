class Emp:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = int(pay)
		self.email = f"{first}.{last}@company.com"

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


class Developer(Emp):
	raise_amt = 1.08

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang


class Manager(Emp):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print(emp.fullname())


dev_1 = Developer('John', 'K', '50000', 'Python')
emp_2 = Emp('Jane', 'M', 50000)
mgr_1 = Manager('Tom', 'H', 90000, [dev_1])


print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Developer))


# # print(mgr_1.email)
# mgr_1.add_emp(emp_2)

# mgr_1.remove_emp(dev_1)

# mgr_1.print_emps()


