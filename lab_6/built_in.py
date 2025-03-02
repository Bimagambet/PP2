# task-1
def multiply_list(lst):
    ans = 1
    for i in lst:
        ans*=i
    return ans

list = [7,7,7]
print(multiply_list(list))

# task-2
def sanau(text):
    up = 0
    low = 0
    for i in text:
        if ord(i) > 96:
            low += 1
        else:
            up += 1
    return up, low

print(sanau("SULTANsultan"))

# task-3
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("alla"))

# task-4
import time
import math

def square(num, uaqyt):
    time.sleep(uaqyt/1000)
    return math.sqrt(num)

print(square(25100, 2123))

# task-5
def alltrue(a):
    return all(a)

t = (True, True, False, True)

print(alltrue(t))
