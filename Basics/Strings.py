# Strings in Python
# Multiline Strings
from re import A


paragraphs = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer rhoncus ut eros et faucibus. Proin sit amet interdum lacus. Vestibulum ac ligula massa. Mauris facilisis nibh eu imperdiet finibus. Sed sem mi, hendrerit sit amet nunc eu, rhoncus venenatis nibh. Vestibulum sit amet condimentum risus, vitae vulputate odio. Vivamus ex dolor, interdum in augue ut, elementum sodales magna. Quisque aliquet lectus a mauris ornare, sed sodales nulla vulputate. Phasellus ornare porttitor magna et maximus. Phasellus elit nulla, ultricies non viverra non, fermentum et tortor. Quisque pulvinar egestas urna, vitae egestas orci facilisis ac. Cras luctus felis vitae libero vehicula, sed dapibus libero fringilla. Phasellus vitae dolor suscipit, vestibulum leo at, dictum metus. Etiam nec nibh non nibh pretium hendrerit. Aliquam non eleifend purus, nec viverra nisl. Nam non dui laoreet, venenatis eros ut, eleifend arcu.

Vivamus viverra turpis eu metus pretium consequat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras dignissim nisl sapien, vel pulvinar ligula dapibus vitae. Nullam sed viverra dui, ac pharetra tellus. Vestibulum sit amet ex at erat tincidunt viverra. Vivamus ullamcorper lorem sed erat bibendum varius eu quis diam. Suspendisse massa est, eleifend venenatis dolor faucibus, sagittis vulputate sem. Suspendisse facilisis massa vel libero dapibus vehicula. Praesent varius venenatis tortor.

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nulla bibendum nisl ut rhoncus semper. In facilisis sed augue id gravida. Nulla enim enim, posuere at gravida et, egestas quis est. Vestibulum condimentum id velit nec maximus. Vivamus ullamcorper malesuada pellentesque. Vestibulum consequat, orci a convallis interdum, massa ligula fringilla magna, eleifend molestie est justo eget nunc. Donec erat elit, congue in condimentum eu, mattis interdum ipsum. Mauris nunc est, sollicitudin eget enim sed, porta sodales mauris. Nullam eget odio purus. Quisque porttitor luctus ullamcorper. Sed porta dolor efficitur, finibus nunc ut, rhoncus sapien. 
"""

print(paragraphs)

print("-- --")

# Playing with Strings
aSampleString = "This is some random string"

# Slicing strings
print(aSampleString [:4]) # From Index 0 (start) to Index 3 (4th index is not included)
print(aSampleString [8:]) # From Index 8 to the end of the string
print(aSampleString [8: 12]) # From Index to Index
print(aSampleString [-6 : -3]) # From Index -6 ( ) to Index -3 (r)

print("-- --")

# Modify Strings
print("I like caps".upper()) # Uppercase
print("I DONT like caPS".lower()) # Lowecase
print("   Get rid of any extra whitespaces bef/end    ".strip()) # Remove extra whitespaces from the beginning and the end 
print("I like oranges".replace("oranges", "watermelons")) # Replace some string with another string
print("Hello My Name is Mafee7".split(" ")[4]) # Split the string into a list at a specific charecter (space here)
print(len("Hello")) # Length of the string

# See /Extra/stringmethods.py for more!