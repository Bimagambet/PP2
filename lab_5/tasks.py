import re

with open("C:/Users/Юзер/OneDrive/Рабочий стол/python/PP2/lab_5/row1.txt", "r", encoding="utf-8") as file:
    file_content = file.readlines()
    

# task-1
sample = r"ab*"

for line in file_content:
    match = re.findall(sample, line)
    if match:
        print(f"Matched in line: {line.strip()}")

   
# task-2
sample = r"ab{2,3}"

for line in file_content:
    if re.search(sample, line):
        print(f"Matched in line: {line.strip()}")
    
# task-3
sample = r"[a-z]+_[a-z]+"

for line in file_content:
    matches = re.findall(sample, line)
    if matches:
        print(f"Matched in line: {line.strip()}")
    
# task-4
sample = r"[A-Z][a-z]+"

for line in file_content:
    matches =  re.findall(sample, line)
    if matches:
        print(f"Matched in line: {line.strip()}")

# task-5
sample = r"a.*b$"

for line in file_content:
    if re.search(sample, line):
        print(f"Matched in line: {line.split()}")
    
# task-6
sample = r"[ ,.]"

modified1 = []

for line in file_content:
    modified1.append(re.sub(sample, ":", line))
    

for line in modified1:
    print(line.strip())
    
# task-7
test_strings = [
    "hello_world",
    "python_programming",
    "convert_snake_case",
    "snake_case_example",
    "alreadyCamelCase"
]
for line in test_strings:
    camel_case = re.sub(r'_([a-z])' , lambda x: x.group(1).upper(), line.capitalize())
    print(camel_case.strip())
        
# task-8
sample = r"(?=[A-Z])"
modified = []
for line in file_content:
    modified.append(re.split(sample, line))
print(modified)

# task-9
sample = r"(?<!^)(?=[A-Z])"

test_strings = [
    "HelloWorld",
    "PythonIsFun",
    "InsertSpacesBeforeUpperCase",
    "camelCaseExample",
    "NoUppercase"
]


modified2 = []
for line in test_strings:
    modified2.append(re.sub(sample, " ", line))

for lines in modified2:
    print(lines)

# task-10
modified3 = []

test_strings = [
    "HelloWorld",
    "PythonIsFun",
    "ConvertCamelCase",
    "camelCaseExample",
    "NoUppercase"
]

for line in test_strings:
    modified3.append(re.sub(r'(?<!^)([A-Z])', r'_\1', line).lower())
    
for lines in modified3:
    print(lines)