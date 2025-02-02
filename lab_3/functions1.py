import math
import re


# task-1
def grams_to_ounces(gramdar):
    return gramdar * 28.3495231

# gramdar = float(input("gramdar jaz"))
# print(f"{grams_to_ounces(gramdar)} ounces")

# task-2
def fran_to_celsi(fara):
    return (5/9) * (fara - 32)

# fara = float(input("ne stoit temperaturit Jackie Chan"))
# print(f"{fran_to_celsi(fara) :.2f} Celsius")

# task-3
def QORA(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            return chickens, rabbits
    return "no solution"

# print(QORA(35, 94))

# task-4
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def filter(num):
    #return [n for n in num if is_prime(n)]

    primes = []
    
    for n in num:
        if is_prime(n):
            primes.append(n)
            
    return primes

# list = [3, 8, 12, 19, 22, 25, 27, 30, 33, 35, 37, 2, 5, 15, 39]

# optimus = filter(list)

# print("optimus", optimus)

# task-5

def S_pernutation(s):
    if len(s) == 0:
        return [s]
    ans = []
    for i in range(len(s)):
        for x in S_pernutation(s[:i] + s[i+1:]):
            ans.append(s[i] + x)
    
    return ans
            
# print(S_pernutation("hello"))

# task-6
def rev(str):
    ans = str.split()
    ans.reverse()
    print(*ans)
    
# string = input("write: ")
# rev(string)


# task-7
def has_33(num):
    
    for i in range(1, len(num)):
        if(num[i] == 3 and num[i] == num[i - 1]):
            # print("true")
            return True
        
    # print("false")
    return False

# has_33([1, 3, 3]) 
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3]) 
         
# task-8
def spy_game(nums):
    zero = 0
    for i in nums:
        if(i == 0):
            zer+=1
        elif(zer == 2 and i == 7):
            # print("true")
            return True
    # print("false")
    return False
    
# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7]) 
# spy_game([1,7,2,0,4,5,0])

# task-9
def volume(r):
    return ((4/3) * math.pi * (r ** 3))
    
# r = float(input("san jaz"))
# print("volume is ", f"{volume(r):.2f}" )

# task-10
def unique(list):
    ans = []
    for i in list:
        if i not in ans:
            ans.append(i)
    
    return ans

# print(unique([1, 2, 2, 3, 4, 4, 5])) 

# task-11
def palindrom(soz):
    soz = re.sub(r'^a-zA-Z', '', soz)
    if(soz == soz[::-1]):
        # print("yes")
        return True
    # print("no")
    return False

# palindrom("kazak")
# palindrom("Kazak")

# task-12
def histogram(zuldyz):
    for repeat in zuldyz:
        print("*" * repeat)        

# histogram([4, 8])

# task-13
"""
import random

name = input("Hello! What is your name?")
print("Well," ,f"{name}", "I am thinking of a number between 1 and 20.")
secret = random.randint(1, 20)

cnt = 0

while True:
    print("Take a guess.")
    user_num = int(input())
    cnt += 1
    
    if(secret > user_num):
        print("Your guess is too low.")
    elif(secret < user_num):
        print("Your guess is too high.")
    else:
        print("Good job,", f'{name}', "You guessed my number in", f'{cnt}', "guesses!")
        break
"""


