import time
import math

def nchooser(n,r):
    f = math.factorial
    return f(n)/f(r)/f(n-r)

def main():
    start=time.time()
    answer=nchooser(40,20)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
1000000