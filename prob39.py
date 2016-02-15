import time
from math import sqrt

def numtrianglesolutions(num):
    count=0
    for j in range(1,(int(sqrt(num))+1)/4):
        for k in range(j+1,(int(sqrt(num))+1)/4):
            n=1
            while n*(2*k**2+2*k*j)<num:
                n+=1
            if n*(2*k**2+2*k*j)==num:
                count=count+1
    return count
    
def mostsolutions(maxval):
    highest,index=0,0
    for num in range(maxval+1):
        thisnum=numtrianglesolutions(num)
        if thisnum>highest:
            highest=thisnum
            index=num
    return index
    
def main():
    start=time.time()
    answer=mostsolutions(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
                

