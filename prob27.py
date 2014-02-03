from math import sqrt,fabs

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

def quad(a,b,n):
	return n*n+a*n+b

top=0
product=0
for a in range(-999,1000):
	for b in range(-999,1000):
		count=0
		n=0
		while isprime(fabs(quad(a,b,n))):
			count=count+1
			n=n+1
		if count>top:
			top=count
			product=a*b
print top
print product
