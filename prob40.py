import time

def makeconstant():
    d='.'
    i=1
    while len(d)<1000001:
        d=d+str(i)
        i+=1
    return d
    
def digitproduct(d):
    return int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000])

def main():
    start=time.time()
    answer=digitproduct(makeconstant())
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()