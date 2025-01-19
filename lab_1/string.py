#1
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

for x in "banana":
  print(x)
  
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#2
b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[-5:-2])

#3
a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

#4
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#5
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#6
txt = "We are the so-called \"Vikings\" from the north."
print(txt)