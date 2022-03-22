# Useful String Methods in Python

print("This is Centered".center(50)) # Center a string between some spaces
print("Hi Hi Hi Hi Hi Hi Hi Hello Hi Hi".count("Hi")) # Count the Occurances of "Hi"
print("एन्कोडेड".encode()) # UTF Encode string
print("This String Starts With This?".startswith("This")) # Checks if the string starts with This
print("Ends with monke?".endswith("?")) # Checks if the string ends with ?
print("Expand Tab size here: \t monke".expandtabs(5)) # Expand the Tab size to 5 when \t is used
print("Where is monke?".find("monke")) # Get the index of "monke"
print("128345526878590".find("8", 0, 5)) # Get the index of the string if it is between Index 0 and 5
print("We have {nos} {item} (s) in stock".format(nos = 13, item = "GPU")) # [USEFUL++] format the string to be with the new values
print(" | ".join(("Candy", "Doughnut", "Butter"))) # Join all the items of an iterable to the string
print("Hi\nmonke\n python".splitlines()) # Splits all lines of a string into a list

# @Ref https://www.w3schools.com/python/python_ref_string.asp