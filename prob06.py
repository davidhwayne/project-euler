import time

def computation(n):
    return (3*(n**4)+2*(n**3)-3*(n**2)-2*n)/12

def main():
    start=time.time()
    answer=computation(100)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()