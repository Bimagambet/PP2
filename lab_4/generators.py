n = int(input("="))

# task-1
print("task-1")
for i in range(1, n+1):
    print(i*i)
print()

# task-2
print("task-2")
for i in range(1, n+1,):
    if i % 2 == 0:
        print(i, end=" ")
print()

# task-3
print("task-3")
for i in range(1, n+1):
    if i % 3 == 0 and i % 4 == 0:
        print(i, end=" ")
print()

# task-4
print("task-4")
a = 5
b = 9
for i in range(a, b+1):
    print(i*i, end=" ")
print()

# task-5
print("task-5")
for i in range(n, 0, -1):
    print(i, end=" ")
    
