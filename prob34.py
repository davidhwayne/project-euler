import time
from math import factorial

def sumfactorialsums():
    return sum([sum([factorial(int(digit)) for digit in str(num)]) for num in range(3,300000) if sum([factorial(int(digit)) for digit in str(num)])==num])

def main():
    start=time.time()
    answer=sumfactorialsums()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
    
