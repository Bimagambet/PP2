nums = [1,2,3,4,5,6,7,8]
res = map(lambda x: x ** 2  , nums)
print(list(res))

even = filter(lambda x: x % 2 == 0, nums)
print(list(even))