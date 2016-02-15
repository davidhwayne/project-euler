import time
from math import sqrt,log

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist
    
def primenumbertheorem(num):
    return num*log(num)

def main():
    start=time.time()
    epsilon=2000
    answer=primes(int(primenumbertheorem(10000+epsilon)))[10000]
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()

