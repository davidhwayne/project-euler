import time

def isamicable(n):
    sumdiv=sum([j for j in range(1,int(n/2)+1) if n%j==0])
    if n==sumdiv:
        return (False,-1)
    else:
        othersum=sum([k for k in range(1,int(sumdiv/2)+1) if sumdiv%k==0])
        if othersum==n:
            return (True,sumdiv)
        else:
            return (False,-1)

def findamicables(upto):
    ams=[]            
    for i in range(1,upto):
        if i in ams:
            continue
        amicable=isamicable(i)
        if amicable[0]:
            ams+=[i,amicable[1]]
    return ams
        
def main():
    start=time.time()
    answer=sum(findamicables(10000))
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
