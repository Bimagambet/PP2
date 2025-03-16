# DATE

import datetime 
# task-1 
# cur_date = datetime.datetime.now()
# after_five_day = cur_date - datetime.timedelta(day = 5)
# print(after_five_day)

# task-2
# import datetime
# today = datetime.datetime.now()
# yesterday = today - datetime.timedelta(days = 1)
# tommorow = today - datetime.timedelta(days = 1)

# print(yesterday.strftime("%Y-%B-%d"))
# print(today.strftime("%Y-%B-%d"))
# print(tommorow.strftime("%Y-%B-%d"))

# task-3
# cur_date = datetime.datetime.now()
# print(cur_date.replace(microsecond=0))

# task-4
# firstdate1 = datetime.datetime(2025, 2, 12, 0, 0, 25)
# secondtime2 = datetime.datetime(2025, 2, 12, 0, 0, 0)
# print(abs(firstdate1-secondtime2).total_seconds())

# GENERATORS
# n = int(input("="))

# # task-1
# print("task-1")

# for i in range(1, n+1):
#     print(i*i)
# print()

# # task-2
# print("task-2")

# for i in range(1, n+1,):
#     if i % 2 == 0:
#         print(i, end=" ")
# print()

# # task-3
# print("task-3")

# for i in range(1, n+1):
#     if i % 3 == 0 and i % 4 == 0:
#         print(i, end=" ")
# print()

# # task-4
# print("task-4")
# a = 2
# b = 7
# for i in range(a, b+1):
#     print(i * i, end=" ")
# print()

# # task-5
# print("task-5")
# for i in range(n, 0, -1):
#     print(i, end=" ")
    
# MATH
import math
# task-1
# n = int(input("Input degree: "))
# print("Output: ", n * (math.pi / 180))

# task-2
# h = int(input("h="))
# b1 = int(input("b1="))
# b2 = int(input("b2="))

# print(((b1 + b2) * h)/2)

# task-3
# n = int(input("num of side="))
# s = int(input("len of side="))
# # math.ceil
# print(math.floor((n * s * s) / (4 * math.tan(math.pi/n))))

# task-4
# b = int(input("Lenght of base: "))
# h = int(input("Height of parallelogram: "))
# print("Expected Output:", b*h)

import json

# JSON as a string
toy_box_json = '{"toys": [{"name": "Teddy Bear", "color": "Brown"}, {"name": "Car", "color": "Red"}, {"name": "Doll", "color": "Pink"}]}'

toy_box = json.loads(toy_box_json)
print(toy_box['toys'][0]["name"])

new_json = json.dumps(toy_box, indent=4)
print(new_json)