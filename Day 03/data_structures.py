# '''
# a data structure is a data organization, 
# management, and 
# storage format that enables efficient access and modification.
# '''

# # message = 'Hello, Hi'
# # message = ['Hello', 'Hi']
# # message.append('Hey')

# # print(message)



# # print(message[7:9])

# # [start:stop]
# # print(message[1])


# courses = ['maths', 'Physics', 'CompSci']
# message = ['Hello', 'Hi']

# # courses.remove('maths')
# removed = courses.pop(1)
# # courses.append(message)
# # courses.insert(0,'CompSci')
# # courses.extend(message)

# print(removed)

# print(courses)

# nums = [2,5,1,3,4]

# # nums.sort()

# sorted_nums = sorted(nums)

# print(sorted_nums)


# courses = ['maths', 'Physics', 'CompSci']
# print(courses.index('Physics'))



# in

# print('maths' in courses)

# for index, value in enumerate(courses):
# 	print(index, value)

# message = 'Hello, Hi'

# message_list = message.split(' , ')

# print(message_list)

# print(type(message))
# print(type(message_list))

# message_str = ' - '.join(message_list)
# print(message_str)

# # Mutable

# list_1 = ['maths', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Bio'

# print(list_1)
# print(list_2)


# # Immutable
# tuple_1 = ('maths', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Bio'

# print(tuple_1)
# print(tuple_2)


# Sets

# courses = {'maths', 'Physics', 'CompSci', 'maths', 'maths'}

# print('CompSci' in courses)


# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Set
# empty_set = {} #This is also used for creating Dict
# empty_set = set()


# Dict --> Key:value

emp = {'name':'Tom', 'age': 27, 'prog_lang':['Python', 'JS']}


# print(emp.keys())
# print(emp.values())
# print(emp.items())

for keys, values in emp.items():
	print(keys, values)



# emp['email'] = 'tom@company.com'
# emp['name'] = 'Jane'

# emp.update({'name':'Jake', 'email':'j@company.com'})

# del emp['age']
# age = emp.pop('age')

# print(emp)
# print(emp.get('email'))