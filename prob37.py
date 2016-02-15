import time

def primes(n):
    sieve=[True]*n
    for i in range(2,n):
        if sieve[i]:
            for j in range(2*i,n,i):
                sieve[j]=False 
    primelist=[num for num,boo in enumerate(sieve) if boo and num>1]
    return primelist

def istrunc(n,primes):
    p=str(n)
    if len(set(['0','2','4','5','6','8'])&set(p[1:]))>0:
        return False
    for k in range(len(p)):
        lefttr=int(p[k:])
        righttr=int(p[:len(p)-k])
        if int(lefttr) not in primes:
            return False
        if int(righttr) not in primes:
            return False
    else:
        return True

def truncs():
    primelist=primes(1000000)
    truncs=[]
    i=4
    count=0
    while count<11:
        if istrunc(primelist[i],primelist):
            truncs.append(primelist[i])
            count+=1
        i+=1
    return sum(truncs)
    
def main():
    start=time.time()
    answer=truncs()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()


