try:
    f = open("lab_6/names.txt")
    print(f.read())
except:
    print("the file didn t found")
finally:
    f.close()
    
# print("hello sultan")f