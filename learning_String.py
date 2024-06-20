# Strings are any sequence of characters(letters, numerals) enclosed in single or double quotes.

# 1- concatenating Strings and Variables with the print function

# 1.1 concatenating using a comma
name = "Zen"
print("My name is", name)

# 1.2 concatenating using a plus sign

name = "Maria"
print("My name is " + name)

# concatenating string and number
name = "67"
number = 4
# type casting or explicit type conversion
print( name + " " + str(number))

print (int(name) + number)


# String interpolation

# 2.1 F-Strings(Literal String Interpolation)
first_name = "Zen"
last_name = "Coder"
age = 89
print(f"My  name is {first_name} {last_name} and I am {age}years old.")

# string.format"()
first_name = "Zoe"
last_name = "Henry"
age = 76
print("My name is {} {} and I am {} years old." .format(first_name, last_name, age))
print("My name is {} {} and I am {} years old." .format(age, last_name, first_name))