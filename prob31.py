import time

def countways(value):
    count=1
    for i in range(201):
        a=200-i
        for j in range(a/2+1):
            b=a-2*j
            for k in range(b/5+1):
                c=b-5*k
                for l in range(c/10+1):
                    d=c-10*l
                    for m in range(d/20+1):
                        e=d-20*m
                        for n in range(e/50+1):
                            f=e-50*n
                            for o in range(f/100+1):
                                total=i+2*j+5*k+10*l+20*m+50*n+100*o
                                if total==value:
                                    count=count+1
    return count
    
def main():
    start=time.time()
    answer=countways(200)
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()

