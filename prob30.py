import time

def sumfifth():
    return sum([sum([int(digit)**5 for digit in str(num)]) for num in range(2,400000) if sum([int(digit)**5 for digit in str(num)])==num])

def main():
    start=time.time()
    answer=sumfifth()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
    

