import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist

def trianglemaxnumdivs(maxnum):
    primelist=primes(100)
    n=2
    while n>0:
        k=(n*(n+1))/2
        count=2
        for i in primelist:
            if i>k:
                break
            power=0
            while k%(i**(power+1))==0:
                power=power+1
            count=count*(power+1)
        if count>maxnum:
            break    
        n=n+1
    return k
    
def main():
    start=time.time()
    answer=trianglemaxnumdivs(500)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()