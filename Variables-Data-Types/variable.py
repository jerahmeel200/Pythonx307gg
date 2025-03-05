x = 5
y = "john"

print(x) # output 5
print(y) # output john


# Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.

x = 4
x = "Sally"
print(x) # output sally

 
#If you want to specify the data type of a variable, this can be done with casting.

x =  str(3) # output 3
y = int(3) # output 3
z = float(3) # output 3.0



#Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Illegal variable names:

# 2myvar = "John"
# my-var = "John"
# my var = "John"


# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"


# Assign Multiple Values
# Python allows you to assign values to multiple variables in one line:

x,y,z = "orange", "banana", "cherry" 
#Note: Make sure the number of variables matches the number of values, or else you will get an error.
print(x)
print(y)
print(z)


# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:
x=y=z = "orange" 
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to
# extract the values into variables. This is called unpacking.

# Example
# Unpack a list:

fruit = ["apple", "banana", "cherry"]
x=y=z = fruit
print(x)
print(y)
print(z)


# Output Variables
# The Python print() function is often used to output variables.

x = "Python is awesome"
print(x)
# In the print() function, you output multiple variables, separated by a comma:
x = "python"
y = "is"
z = "awesome"
print(x,y,z)

# You can also use the + operator to output multiple variables:
x = "python"
y = "is"
z = "awesome"
print(x + y + z)

# For numbers, the + character works as a mathematical operator:

# Example
x = 5
y = 10
print(x + y)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:

# The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:

# Example
x = 5
y = "John"
print(x, y)
