# mytuple = ("apple" , "banana")
# myit = iter(mytuple)
# # print(next(myit))
# # print(next(myit))
# for x in mytuple:
#     print(x)

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)

class vehicle:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("move!")
        
class car(vehicle):
    pass

class boat(vehicle):
    def move(self):
        print("sail!")
        
class plane(vehicle):
    def move(self):
        print("fly!")
        
car1 = car("ford", "mustang")
boat1 = boat("rag", "558")
plane1 = plane("boeing", "448")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
