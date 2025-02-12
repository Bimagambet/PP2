import math

class cars():
    def __init__(self, brend, mark):
        self.brend = brend
        self.mark = mark
    def __str__(self):
        return f"{self.brend}{" "}{self.mark}"
    
    def myfunc(selfemes):
        print("hello my car is " + selfemes.brend + " " + selfemes.mark)
        
class diller(cars):
    def __init__(self, brend, mark, year):
        super().__init__(brend, mark)
        self.year = year
        
    def salon(self):
        print("we have " + self.brend + " " + self.mark + " " + self.year)

x = diller("lamborghini", "urus", "2020")
x.salon()
"""
"""
class task1:
    def __init__(self):
        self.qaz = ""
    def getstring(self):
        self.qaz = input("input smth: ")
    def printstring(self):
        print(self.qaz.upper())
        
c1 = task1()
c1.getstring()  
c1.printstring()        
"""
"""
class shape():
    def __init__(self, a = 0, b = 0):
        self.lenght = a
        self.width = b
    def area(self):
        print(self.lenght * self.width)
    
class square(shape):
    def __init__(self, a=0, b=0):
        super().__init__(a, b)
    def areaSQ(self):
        print(self.lenght * self.lenght)
        
sh = shape(5, 6)
sh.area()

sq = square(sh.lenght)
sq.areaSQ()
"""
"""
class rectangu():
    def __init__(self, len, wid):
        self.len = len
        self.wid = wid
    def area(self):
        print(self.len * self.wid)
        
a1 = rectangu(6, 2)
a1.area()
"""
"""
class points():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x, self.y)
    def move(self, movex, movey):
        self.x = movex
        self.y = movey
    def dist(self, otherpoint):
        print(math.sqrt((otherpoint.x - self.x) ** 2 + (otherpoint.y - self.y) ** 2))
        
p1 = points(2, 9)
p2 = points(7, 6)

p1.show()
p1.move(2, 5)
p1.show()

p1.dist(p2)
"""
"""
class account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, cashin):
        self.balance += cashin
        print("you have " , self.balance)
    def withdraw(self, cashout):
        if self.balance >= cashout:
            self.balance -= cashout
            print("you have " , self.balance)
        else:
            print("you dont have enough money")
            
g1 = account("sultan", 1000)
g1.deposit(1000)
g1.withdraw(2100)
g1.withdraw(900)


def isprime(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

numlist = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

ans = list(filter(lambda x: isprime(x), numlist))
print(ans)  










