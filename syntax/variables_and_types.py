# completely object oriented
# do not need to declare variables before using them, or declare their type
# every variable in Python is an object

# supports two types of numbers - integers and floating point numbers

# printing an integer
myint = 7
print(myint)

# printing a float can be done in two ways
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# string are defined with either single or double qoutes
# double qoutes are easier to work with as inserting ' wouldn't close the string like it would when using ''
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# assignments can be done on more than one variable simultaneously
a,b = 0, 3
print(a)
print(b)


# Mixing operators between numbers and strings is not supported
print(1 + "hello" + 5) # causes a type error

