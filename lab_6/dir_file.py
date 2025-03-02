import os

#useful info
# os.listdir(path): Shows everything inside a folder.
# os.path.isdir(path): Checks if something is a folder.
# os.path.isfile(path): Checks if something is a file.


# task-1
# def content_list(path):
#     all_items = os.listdir(path)
    
#     directories = []
#     files = []
    
#     for zat in all_items:
#         full_path = os.path.join(path, zat)
#         if os.path.isdir(full_path):
#             directories.append(zat)
#         elif os.path.isfile(full_path):
#             files.append(zat)
    
#     print("Directories:", directories)
#     print("Files:", files)
#     print("All items:", all_items)
    
# path = "."
# content_list(path)

# task-2
# path = "sultan.txt"
# # path = "."
# print('Exist:', os.access(path, os.F_OK))
# print('Readable:', os.access(path, os.R_OK))
# print('Writable:', os.access(path, os.W_OK))
# print('Executabler:', os.access(path, os.X_OK))

# task-3
# path = "names.txt"
# if os.path.exists(path):
#     print(os.path.dirname(path))
#     print(os.path.basename(path))
# else:
#     print("path does't exist")

# task-4
# path = "names.txt"

# with open(path, 'r') as file:
#     lines = file.readlines()
#     num = len(lines)

# print(num)

# task-5
# list = [1,2,3,4,5,6,7]
# with open('text_file.py', 'w') as file:
#     for i in list:
#         file.write(str(i) + '\n')
        
# task-6
for i in range(65, 91):
    name = f"{chr(i)}.txt"
    with open(name, 'w') as f:
        f.write(chr(i))
        
# task-7
with open('names.txt', 'r') as file:
    content = file.read()
with open('new_names.txt', 'w') as file:
    file.write(content)
    
# task-8
file_path = 'A.txt'
if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        os.remove(file_path)
    else:
        print("Permition denied")
else:
    print("does not exist")
    
    