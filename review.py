first_name = "Alana"
last_name = "Da Silva"
age = 38
profession = "Software Developer"
years_experience = 5
greeting = "Hello my name is ", first_name, last_name
print(greeting)

print("I am {age} years old")

print("I work as a profession {}" .format(profession))

exp_string = "I have worked in the field for {} years."
print(exp_string.format(age))

print("I started in the field when I was " + str(age - years_experience) + " years old.")