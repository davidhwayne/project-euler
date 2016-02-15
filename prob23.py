import time

def isabundant(n):
    if n<sum([j for j in range(1,int(n/2)+1) if n%j==0]):
        return True
    else:
        return False

def findabundants(upto):
    return [i for i in range(1,upto) if isabundant(i)]

def getpairwisesums(nums,maxnum):
    pairsums=[]
    for i,n in enumerate(nums):
        if n>maxnum/2:
            break
        for m in nums[i:]:
            pairsums.append(n+m)
    return pairsums

def sumnotin(numlist,maxnum):
    return sum(set(range(1,maxnum))-set(numlist))

def main():
    start=time.time()
    answer=sumnotin(getpairwisesums(findabundants(28123),28123),28123)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()


