import time

def longseq(upto):
    most,top=0,1
    for n in range(1,upto):
        count,i=0,n
        while i!=1:
            count=count+1
            if i%2==0:
                i=i/2
            else:
                i=3*i+1
        if count>most:
            most,top=count,n
    return top

def main():
    start=time.time()
    answer=longseq(1000000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()
