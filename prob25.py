import time

def fibgenerator():
    index=3
    f1,f2=1,1
    while True:
        next=f1+f2
        yield (next,index)
        f1,f2=f2,next
        index+=1
    
def getfibdigits(numdigits):
    fibval=fibgenerator()
    generatedval=fibval.next()
    outputval=0
    while len(str(generatedval[0]))<numdigits:
        generatedval=fibval.next()
    return generatedval[1]

def main():
    start=time.time()
    answer=getfibdigits(1000)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()