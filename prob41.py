import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist
    
def ispan(n):
    s=set(str(n))
    if s==set([str(i) for i in range(1,8)]):
        return True
    else:
        return False

def largesstpanprime():
    primelist=primes(7654322)
    for p in primelist[::-1]:
        if ispan(p):
            return p

def main():
    start=time.time()
    answer=largesstpanprime()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
    
