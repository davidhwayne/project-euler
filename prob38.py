import time

def ispan(n):
    s=set(str(n))
    if s==set([str(i) for i in range(1,10)]):
        return True
    else:
        return False

def largestpan():
    current=918273645
    for i in range(9876,9182,-1):
        new=str(i)+str(i*2)
        if ispan(new):
            return new   

def main():
    start=time.time()
    answer=largestpan()
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()