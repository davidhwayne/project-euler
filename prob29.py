nums=[4]
for i in range(2,101):
	for j in range(2,101):
		n=i**j
		index=0
		while n<=nums[index]:
			if n==nums[index]:
				break
			else:
				index+=1
		else:
			nums.insert(index,n)
print len(nums)
