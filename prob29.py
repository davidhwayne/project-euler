import time

def distinctnums(maxnum):
    nums=[4]
    for a in range(2,maxnum+1):
        for b in range(2,maxnum+1):
            n=a**b
            nums.append(n)
    return len(set(nums))

def main():
    start=time.time()
    answer=distinctnums(100)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()