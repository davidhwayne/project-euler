import time

def last10():
    sum=0
    for i in range (1,1001):
        sum=(sum+(i**i))%10000000000
    return sum
    
def main():
    start=time.time()
    answer=last10()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
