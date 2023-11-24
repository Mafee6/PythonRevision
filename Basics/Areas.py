from math import pi as PI;

# Unit 
unit = "cm²"

# Area of a 10 x 10 Square
s = 10
area = s * s
print("Area of a {s} x {s} Square = {area}{unit}".format(s = s, area = area, unit = unit))

# Area of a 5 x 6 Rectangle
l = 5
b = 6
area = l * b
print("Area of a {l} x {b} Rectangle = {area}{unit}".format(l = l, b = b, area = area, unit = unit))

# Area of a Triangle of Base: 3 and Height 8
b = 3
h = 8
area = (1 / 2) * b * h
print("Area of a Triangle of Base {b} & Height {h} = {area}{unit}".format(b = b, h = h, area = area, unit = unit))

# Area of a Circle of Radius 9
r  = 9
area = PI * (r * r)
print("Area of a Circle of Radius {r} = {area}{unit}".format(r = r , area = area, unit = unit))

# Area of a Hexagon of side 5
# 2.59807621135 = (3 * cbrt(3)) / 2
s = 5
area = 2.59807621135 * (s * s)

print("Area of a Hexagon of side {s} = {area}{unit}".format(s = s, area = area, unit = unit))