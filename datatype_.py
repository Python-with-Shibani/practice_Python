# Basic datatypes in python
a = 22
print(type(a))

b = 3.14
print(type(b))

c = "Bangalore"
print(type(c))

d = True
print(type(d))

e = 2+5j
print(type(e))

# primitive or basic datatypes are immutable i.e as one changes the variable value new address wil be created (new object)
a = 22
print(id(a))
a = 44
print(id(a))

# using indexes we can get the elements of a string
c = "Bangalore"
print(c[0])
# c[0] = "M"  will not change due to immutablility
# print(c) 

# falsy values in bool are 0, [], none, False, "" other than these are true values

print(bool(-22))

# typecasting/conversion of datatype
print(int(123.456))  # int will convert best 10
print(int("22"))
print(int(True))
print(int(False))

# print(int("10.89"))

print(float("10.89"))
print(float(22))
print(float(True))
print(float("22"))


print(bool(12))
print(bool("name"))
print(bool(1+2j))
print(bool(0))
print(bool(None))
#print(bool(j))  (invalid as j is not defined)

print(str(1))
print(str(True))
print(str(12.7))
print(str(1+2j))
a = True
print(type(a))
b = str(a)
print(type(b))
c = 1
print(type(c))
d = str(c)
print(type(d))

city = "BANGLORE"
print(city[3])
print(city[-3])

#SLICING (string_name[start:end+1:step])
print(city[1:6])
print(city[0:6:2])
print(city[-8:-4])
# default value for start = 0, end = length of value, step = 1
print(city[ : : ])
print(city[1:100])
# one liner code for reversig the string
print(city[ : :-1])

























