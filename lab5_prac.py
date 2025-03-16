import re

with open('salam/row2.txt', "r", encoding='utf-8') as file:
    txt = file.read()
#1 
# pattern = re.findall(r'ab*', txt)
# print(pattern)
# 2
# pattern = re.findall(r'ab{2,3}', txt)
# print(pattern)
# 3
# pattern = re.findall(r'[a-z]+_[a-z]+', txt)
# print(pattern)
# 4
# pattern = re.findall(r'[A-Z][a-z]+', txt)
# print(pattern)
# 5
# pattern = re.findall(r'a.*b', txt)
# print(pattern)
# 6
# pattern = re.sub(r'[ ,.]', '[:]', txt)
# print(pattern)
# 7
# pattern = re.findall(r'[A-Za-z]+_[A-Za-z]+', txt)
# cc = []
# for i in pattern:
#     a = i.split('_')
#     cc.append(a[0] + ''.join(x.capitalize() for x in a[1:]))
# print(cc)
#8
# pattern = re.findall(r'[A-Z][a-z]*', txt)
# print(pattern)
#9
pattern = re.sub(r'(?<!^)(?=[A-Z])', ' ', txt)
print(pattern)
#10