import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist
    
def primedivisors(n,primelist):
    divs=[]
    for testval in primelist:
        if testval>(n/2+1):
            break
        elif n%testval==0:
            divs.append(testval)
    return divs
    
def numpdivs(n,primelist):
    return len(primedivisors(n,primelist))

def consective4():
    primelist=primes(1000)
    n=2*3*5*7
    while True:
        if numpdivs(n+3,primelist)!=4:
            n+=4
        elif numpdivs(n+2,primelist)!=4:
            n+=3
        elif numpdivs(n+1,primelist)!=4:
            n+=2
        elif numpdivs(n,primelist)!=4:
            n+=1
        else:
            return n
def main():
    start=time.time()
    answer=consective4()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()

    


