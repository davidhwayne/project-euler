import time

def sumcomputation(n):
    return sum([i for i in range(n) if i%3==0 or i%5==0])

def main():
    start=time.time()
    answer=sumcomputation(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()