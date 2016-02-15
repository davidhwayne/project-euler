import time
import math

def sumdigits(n):
    return sum([int(i) for i in str(n)])
 
def main():
    start=time.time()
    answer=sumdigits(math.factorial(100))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
