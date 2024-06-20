
# Tuple is a type of data that is immutable and can hold a group of values. Tuples can contain mixed data types.

dog = ('dog', 0, 1, False)
print(dog[2])


#Lists a type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.

empty_list = []
ninjas = ['Rozen', 'John', 'Olivier']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Micheal')
print(ninjas)
ninjas.pop()
print(ninjas)
ninjas.pop(1)
print(ninjas)

#Dictionaries a group key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. When you're ready, you can find more built-in dictionary methods.

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Maria'
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
w = new_person.pop('weight')
print(w)
print(new_person)

print(len(new_person))


int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))
