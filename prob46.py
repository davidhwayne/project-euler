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
    
def oddcomps(n,primelist):
    return [i for i in range(3,n) if i%2==1 and i not in primelist]

def goldbachsum(n,primelist):
    for p in primelist:
        if p>n:
            break
        for i in range(1,int(sqrt(n))+1):
            if p+2*i**2==n:
                return True
    return False
                
def minnotgoldbach():
    primelist=primes(10000)
    odds=oddcomps(10000,primelist)
    for num in odds:
        if goldbachsum(num,primelist):
            continue
        else:
            return num
            
def main():
    start=time.time()
    answer=minnotgoldbach()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()

    



 
