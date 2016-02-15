import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist

def primesanddigits():
    primelist=[p for p in primes(10000) if p>1000]
    digitstonums={}
    for p in primelist:
        primedigits=list(str(p))
        primedigits.sort()
        try:
            digitstonums[''.join(primedigits)].append(p)
        except:
            digitstonums[''.join(primedigits)]=[p]
    return digitstonums

def primediffcycle(primed):
    for digits in primed:
        if len(primed[digits])<3 or 1487 in primed[digits]:
            continue
        primed[digits].sort()
        for i,a in enumerate(primed[digits][:-2]):
            for j,b in enumerate(primed[digits][i+1:]):
                for c in primed[digits][j+1:]:
                    if c-b==b-a:
                        return ''.join([str(p) for p in [a,b,c]])
            
def main():
    start=time.time()
    answer=primediffcycle(primesanddigits())
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
          
