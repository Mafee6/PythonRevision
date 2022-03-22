# Lists in Python
list = ["hi", "bye", "js", "coder", "python"]
print("Original List: " + str(list))

list.append("java") # Append an element in the list
print("After appending an element" + str(list))

list = ["hi", "bye", "js", "coder", "python"]
list.clear() # Remove all the elements of the list
print("After Clearing the list: " + str(list))

list = ["hi", "bye", "js", "coder", "python", "js"]
print(list.count("js")) # Count the no. of occurances of "js" in the list

list1 = ["hi", "bye", "js", "coder", "python"]
list2 = ["i1", "i2", "i3", "i4", "i5"]
list1.extend(list2) # Add the elements of list2 to list1
print(list1)

list = ["hi", "bye", "js", "coder", "python", "binary"]
print(list.index("js")) # Get the index of "js" in the list

list.insert(3, "c++") # Inserts "c++" at the index 3 of the list
print(list)

list.pop(6) # Deleted the element at the 5th index of the list
print(list)

list.reverse() # Now it's Reversed
print(list)

list.sort() # [USEFUL++] Sort the list alphabetically
print(list)

list.sort(reverse = True) # [USEFUL++] Sort the list alphabetically (descending)
print(list)

def sortinFunc (e):
    return len(e)

list.sort(key = sortinFunc) # [USEFUL++] Sort the list using return value of function
print(list)

# Done!