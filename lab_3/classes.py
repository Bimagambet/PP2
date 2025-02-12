import math
# task-1
class Methods():
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Input smth: ")
    
    def printString(self):
        print(self.s.upper())


s = Methods()

s.getString()
s.printString()

# task-2
class Shape():
    def __init__(self, a = 0, b = 0):
        self.length = a
        self.width = b
        
    def getShape(self):
        self.length = int(input("jaz zaebal"))
        self.width = int(input("sende jaz"))
    
    def area(self):
        print(self.length * self.width)

class Square():
    def __init__(self, a):
        self.size = a
    
    def area(self):
        print(self.size ** 2)



shape = Shape()
shape.getShape()
shape.area()


square = Square(4)
square.area()

# task-3
class Rectangle():
    def __init__(self, lenght, width):
        self.length = lenght
        self.width = width


    def area(self):
        print(self.width * self.length)

rectangle = Rectangle(4,5)
rectangle.area()

# task-4
class Points():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)
    
    def move(self, movex, movey):
        self.x = movex
        self.y = movey
    
    def dist(self, otherPoint):
        print(math.sqrt((otherPoint.x - self.x) ** 2 + (otherPoint.y - self.y) ** 2))


point1 = Points(2, 3)
point2 = Points(7, 2)

point1.show()
point1.move(1, 3)
point1.show()

point1.dist(point2)

# task-5
class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, cashin):
        self.balance+=cashin
        print("You have",self.balance)
    
    def withdraw(self, cashout):
        if self.balance >= cashout:
            self.balance -= cashout
            print("You have", self.balance)
        else:
            print("Withdrawals may not exceed the available balance.")


account = Account("asfd", 0)
account.deposit(1000)
account.withdraw(100)
account.withdraw(1000)

# task-6
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 2 == 0:
            return False
    return True

numlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

prime_numlist = list(filter(lambda x: isprime(x), numlist))

print(prime_numlist)