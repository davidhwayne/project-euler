from math import sqrt

primelist=[2]
def isprime(n):	
	global primelist
	prime=False
	for i in range(primelist[len(primelist)-1],int(sqrt(n)+1)):
		for k in primelist:
			if i==k:
				break
			elif i%k==0:
				break
		else:	
			primelist.append(i)
	for k in primelist:	
		if n==k:
			return True
			break
		elif n%k==0:
			return False
	else:
		return True			
		
	
for testval in range(2,int(sqrt(600851475143))+1):
	check=isprime(testval)
	if 600851475143%testval==0 and check:
		primedivisor=testval
		print primedivisor


	
		
