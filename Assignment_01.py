# Module-2: Part-1
#Q1 (format specifier)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hey, %s your age is %i" %(name,age))

#Q2 (f string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hey, {name} your age is {age}")

#Q3 (format method)
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hey, {} your age is {}".format(name,age))

#Q4
a = -5
b = 11.5
c = "Karnataka"
d = False
print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))

#Q5
s = "Python is fun"
print(s)
print("extract from 2nd till 8th: ", s[2:9])
