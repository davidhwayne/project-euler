def permutation(s):
	if len(s)<=1:
		return [s]
	permutations = []
	for l in s:
		subpermut = permutation(s.replace(l, ""))
		for permut in subpermut:
			permutations.append(l + permut)
	return permutations

s10=permutation('0123456789')
s10.sort()
print s10[999999]

