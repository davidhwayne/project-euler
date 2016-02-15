import time

def sumdigits(n):
    return sum([int(i) for i in str(n)])

def main():
    start=time.time()
    answer=sumdigits(2**1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()