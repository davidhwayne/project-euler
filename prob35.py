#This code actually takes a while to compile. 
#This will eventually give an answer, but there is probably a better answer that compiles much quicker.  

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

def rotations(s):
	rotates=[s]
	for i in range(1,len(s)):
		rotates.append(rotates[i-1][1:]+rotates[i-1][0])
	return rotates

primes=primes(1000000)
circulars=[]
for prime in primes:
	cp=rotations(str(prime))
	for rotate in cp:
		if int(rotate) in circulars:
			break		
		i=0
		while primes[i]<int(rotate) and i<len(primes)-1:
			i=i+1
		if primes[i]!=int(rotate):
			break
	else:	
		for rotate in cp:
			if int(rotate) not in circulars:
				circulars.append(int(rotate))
print circulars
print len(circulars)

			



