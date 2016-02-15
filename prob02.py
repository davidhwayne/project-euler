import time

def computesolution(maxval):
    sum,m,n=2,1,2
    for i in range(maxval):
        n,m=n+m,n
        if n%2==0 and n<maxval:
            sum+=n
        elif n>=maxval:
            break
    return sum

def main():
    start=time.time()
    answer=computesolution(4000000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
