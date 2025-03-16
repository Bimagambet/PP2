
# text = {'price', '500', '555', '655', 'agr'}

# pattern = re.findall(r'[0-9]+', text)
# print(pattern)

            
nums = [3, 5, 7, -1, 9]

def all_positivee(nums):
    ans = []
    for i in nums:
        if i > 0:
            ans.append(1)
        else:
            ans.append(0)
    return ans

def all_positive(a):
     return all(a)
 
res = all_positivee(nums)

print(all_positive(res))

 



# # task-5
# def alltrue(a):
#     return all(a)

# t = (True, True, False, True)

# print(alltrue(t))