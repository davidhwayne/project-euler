def permutation(s):
	if len(s)<=1:
		return [s]
	permutations = []
	for l in s:
		subpermut = permutation(s.replace(l, ""))
		for permut in subpermut:
			permutations.append(l + permut)
	return permutations

sum=0
d='0123456789'
for k in range(10):
	if k<9:
		s=d[:k]+d[k+1:]
	else:
		s=d[:k]
	nums=permutation(s)
	for i in nums:
		if int(i[2])%2==0 and int(i[1:4])%3==0 and int(i[2:5])%5==0 and int(i[3:6])%7==0 and int(i[4:7])%11==0 and int(i[5:8])%13==0 and int(i[6:9])%17==0:
			sum=sum+int(str(k)+i)

print sum
