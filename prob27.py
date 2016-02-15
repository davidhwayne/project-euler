import time
from math import sqrt

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist

def isprime(n):        
    if n in primelist:
        return True
    for i in range(primelist[len(primelist)-1],int(sqrt(n)+1)):
        for k in primelist:
            if i%k==0:
                break
        else:        
            primelist.append(i)
    for k in primelist:        
        if n%k==0:
            return False
    else:
        return True                    

def quad(a,b,n):
    return n*n+a*n+b

def topprimeseq(maxmod,primelist):
    baselist=primelist+[-p for p in primelist]
    top=0
    for a in range(-maxmod+1,maxmod):
        for b in baselist:
            n,count=0,0
            while isprime(abs(quad(a,b,n))):
                count=count+1
                n=n+1
            if count>top:
                top=count
                product=a*b
    return product
            
def main():
    start=time.time()
    global primelist
    primelist=primes(1000)
    answer=topprimeseq(1000,primelist)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
