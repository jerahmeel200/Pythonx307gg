# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# You can get the data type of any object by using the type() function:
# example

x = 5
print(type(x)) # output <class 'int'>

x = "Hello World"	#str
print(type(x)) # output <class 'str'>	
x = 20	#int
print(type(x)) # output <class 'int'>	
x = 20.5	#float	
print(type(x)) # output <class 'float'>
x = 1j	#complex	
print(type(x)) # output <class 'complex'>
x = ["apple", "banana", "cherry"]	#list	
print(type(x)) # output <class 'list'>
x = ("apple", "banana", "cherry")	#tuple	
print(type(x)) # output <class 'tuple'>
x = range(6)	#range	
print(type(x)) # output <class 'range'>
x = {"name" : "John", "age" : 36}	#dict	
print(type(x)) # output <class 'dict'>
x = {"apple", "banana", "cherry"}	#set
print(type(x)) # output <class 'set'>
x = frozenset({"apple", "banana", "cherry"})	#frozenset
print(type(x)) # output <class 'frozenset'>	
x = True	#bool	
print(type(x)) # output <class 'bool'>
x = b"Hello"	#bytes	
print(type(x)) # output <class 'bytes'>
x = bytearray(5)	#bytearray	
print(type(x)) # output <class 'bytearray'>
x = memoryview(bytes(5))	#memoryview
print(type(x)) # output <class 'memoryview'>
x = None
print(type(x)) # output <class 'NoneType'>

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	#str
print	
x = int(20)	#int	
x = float(20.5)	#float	
x = complex(1j)	#complex	
x = list(("apple", "banana", "cherry"))	#list	
x = tuple(("apple", "banana", "cherry"))	#tuple	
x = range(6)	#range	
x = dict(name="John", age=36)	#dict	
x = set(("apple", "banana", "cherry"))	#set	
x = frozenset(("apple", "banana", "cherry"))	#frozenset	
x = bool(5)	#bool	
x = bytes(5)	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))
