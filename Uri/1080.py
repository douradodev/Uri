nums =[]
for i in range(100):
	nums.append(int(input()))
print(sorted(nums)[-1])
print(nums.index(sorted(nums)[-1])+1)