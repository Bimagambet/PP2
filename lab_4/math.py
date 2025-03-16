# task-1
import math
n = int(input("Input degree: "))
print("Output radian:", math.radians(n))


# task-2
import math
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("base, second value: "))

print("Expected Output", h/2 * (a + b))


# task-3
import math
n = int(input("Input number of sides: "))
s = int(input("Input the lenght of a side: "))
a = s/2 * math.tan(math.pi/n)
print("Are of the polygon is: ", math.ceil(n*a*s/2))


# task-4
import math
b = int(input("Lenght of base: "))
h = int(input("Height of parallelogram: "))
print("Expected Output:", b*h)