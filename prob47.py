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
n=209
count1=0
count2=0
count3=0
count4=0
for i in primelist:
	if i>213:
		break
	if 210%i==0:
		count2+=1
	if 211%i==0:
		count3+=1
	if 212%i==0:
		count4+=1
while n>0:
	n+=1
	count1=count2
	count2=count3
	count3=count4
	count4=0
	for i in primelist:
		if i>n+3:
			break
		if (n+3)%i==0:
			count4+=1
	if count1>=4 and count2>=4 and count3>=4 and count4>=4:	
		break
print n

	


