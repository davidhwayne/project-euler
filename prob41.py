def primes(n):
	sieve=[True]*n
	for i in range(2,n):
		if sieve[i]:
			for j in range(2*i,n,i):
				sieve[j]=False 
	primelistplus=[]
	n=0
	for boo in sieve:
		if boo:
			primelistplus.append(n)
		n=n+1
	primelist=primelistplus[2:]
			
	return primelist
print 'Generating Primes...'
primes=primes(7654322)

def permutation(s):
	if len(s)<=1:
		return [s]
	permutations = []
	for l in s:
		subpermut = permutation(s.replace(l, ""))
		for permut in subpermut:
			permutations.append(l + permut)
	return permutations

print 'Generating Permutations...'
s7=permutation('1234567')
s7.sort()
print 'Checking..'
k=0
for i in s7[::-1]:
	while int(i)<primes[::-1][k]:
		k=k+1
	if int(i)==primes[::-1][k]:
		print i
		break
	
