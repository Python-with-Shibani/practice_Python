name = "ram"
age = 22
print(name,age)
print("Name is: ", name)
print("Age is: ",age)
print("HI {} your age is {}".format(name,age))
print("HI {0} your age is {1}".format(name,age))
print("Hi {name} welcome for {course}".format(name="Marry",course="python"))
# f string (shortcut for format(replacement operator))
name = 'Marry'
city = 'Bangalore'
print(f'welcome {name} to {city}')
# f string used to evaluate expression
a = 22
b = 44
print(f"addition of {a} and {b} is {a+b}")
# f string used to evaluate function
print(f"Datatype of a is {type(a)}")
