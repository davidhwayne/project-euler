import time

def numremainders(n):
    count=0
    remainders=[]
    q=1
    while True:
        while q<n:
            q=q*10
        if q%n==0:
            count=0
            break
        elif q%n in remainders:
            break
        else:
            q=q%n
            remainders.append(q)
            count+=1
    return count
    
def getmaxremainders(maxnum):
    top,current=0,0
    for i in range(1,maxnum):
        remainders=numremainders(i)
        if top<remainders:
            current=i
            top=remainders
    return current
    
def main():
    start=time.time()
    answer=getmaxremainders(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
