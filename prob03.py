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

def primedivisors(n,type):
    if type=='small':
        prs=primes(int(sqrt(n))+1)
    else:
        prs=primes(n)
    divs=[]
    for testval in prs:
        if n%testval==0:
            divs.append(testval)
    return divs
    
def getanswer(n):
    smallones=primedivisors(n,'small')
    val=n
    for s in smallones:
        val/=s
    if val==1:
        return smallones[-1]
    else:
        return primedivisors(val,'all')[-1]
        
def main():
    start=time.time()
    answer=getanswer(600851475143)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True

main()
        
