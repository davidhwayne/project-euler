import time

def cornersum(iteration):
    return 4*(2*(iteration+1)+1)**2-12*(iteration+1)

def diagsum(size):
    total=1
    iterations=size/2
    for n in range(iterations):
        total+=cornersum(n)
    return total
    
def main():
    start=time.time()
    answer=diagsum(1001)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()