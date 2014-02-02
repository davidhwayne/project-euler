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

primelist=primes(100000)
n=2
while n>0:
	k=(n*(n+1))/2
	count=1
	for i in primelist:
		if i>k:
			break
		power=0
		while k%(i**(power+1))==0:
			power=power+1
		count=count*(power+1)
	if count>500:
		break	
	n=n+1
print "Number: "+str(n)
print "Triangle number: "+str(k)
print "Divisors: "+str(count)
