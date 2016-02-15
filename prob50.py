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
    
def mostconsecutive(primelist):
    top=0
    for i,p in enumerate(primelist):
        count,sum,j=0,0,0
        while sum<1000000:
            sum+=primelist[i+j]
            count+=1
            j+=1
        j-=1
        while sum not in primelist:
            sum-=primelist[i+j]
            count-=1
            j-=1
        if count>top:
            top=count
            topprime=sum
        if sum-p+primelist[i+j+1]>1000000:
            break
    return topprime

def main():
    start=time.time()
    answer=mostconsecutive(primes(1000000))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
