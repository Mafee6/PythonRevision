# Data Types
# Defining Different Types of Variables (added 1 because data type functions)

from xmlrpc.client import boolean


string1 = "some string here" # String
integer1 = 123 # Integer
float1 = 0.46 # Float
complex1 = 10j # Complex (Imaginary Number)
list1 = ["item1", "item2", "item3", "item4"] # List
tuple1 = ("item1", "item2", "item3") # Tuple
range1 = range(10) # Range
set1 = {1, 2, 3, 4, 5} # Set
frozenset1 = frozenset({1, 2, 3, 4, 5}) # Frozen Set
boooleann = False # Boolean
bytez = b"monke" # Bytes
arrayofbytes = bytearray(bytez) # Byte Array
whatismymemoryaddress = memoryview(bytearray(bytez)) # Memory address

# Printing the values (converted to string)

print("String: " + string1)
print("int: " + str(integer1))
print("float: " + str(float1))
print("complex: " + str(complex1))
print("list: " + str(list))
print("tuple: " + str(tuple1)) # I like the name tuple
print("range: " + str(range1))
print("set: " + str(set1))
print("froznset: " + str(frozenset1))
print("bool: " + str(boolean))
print("Bytes: " + str(bytez))
print("Byte Arr: " + str(arrayofbytes))
print("Mem Adrr: " + str(whatismymemoryaddress)) # loong var name