def permutation(s):
	if len(s)<=1:
		return [s]
	permutations = []
	for l in s:
		subpermut = permutation(s.replace(l, ""))
		for permut in subpermut:
			permutations.append(l + permut)
	return permutations

s9=permutation('123456789')
panprod=[]
for i in s9:
	if (int(i[0])*int(i[1:4])==int(i[4:])) and (int(i[4:]) not in panprod):
		panprod.append(int(i[4:]))
	elif (int(i[0])*int(i[1:5])==int(i[5:])) and (int(i[5:]) not in panprod):
		panprod.append(int(i[5:]))
	elif (int(i[0:2])*int(i[2:5])==int(i[5:])) and (int(i[5:]) not in panprod):
		panprod.append(int(i[5:]))
print panprod
print sum(panprod)
		
