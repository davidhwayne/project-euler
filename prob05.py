import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist

def primedecomposition(n):
    divs=[]
    for testval in primes(n+1):
        exponent=0
        while n%(testval**exponent)==0:
            exponent+=1
        divs.append((testval,exponent-1))
    return divs
    
def lcmuptotopnum(topnum):
    alldivs=[]
    for n in range(1,topnum+1):
        alldivs+=primedecomposition(n)
    primemaxexp={}
    for a in alldivs:
        try:
            if primemaxexp[a[0]]<a[1]:
                primemaxexp[a[0]]=a[1]
        except:
            primemaxexp[a[0]]=a[1]
    product=1
    for pe in primemaxexp:
        product*=pe**primemaxexp[pe]
    return product

def main():
    start=time.time()
    answer=lcmuptotopnum(20)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True

main()
        
