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

def rotations(s):
    rotates=[s]
    for i in range(1,len(s)):
        rotates.append(rotates[i-1][1:]+rotates[i-1][0])
    return [int(r) for r in rotates]

def numcirculars(primeset):
    count=0
    for prime in primeset:
        rotates=set(rotations(str(prime)))
        if rotates<primeset:
            count+=len(rotates)
            primeset=primeset-rotates
    return count
    
def main():
    start=time.time()
    answer=numcirculars(set(primes(1000000)))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
            



