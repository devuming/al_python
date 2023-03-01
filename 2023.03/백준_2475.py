pow_2 = lambda x : x**2
nums = list(map(pow_2, map(int, input().split())))
print(sum(nums) % 10)