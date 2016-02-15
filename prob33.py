import time
from fractions import gcd

def lcm(a,b):
    return a*b/gcd(int(a),int(b))

def digitcancel(m,n):    
    ms,ns=str(m),str(n)
    for x in ms:
        for y in ns:
            if x==y and x!=0:
                newms=ms.replace(x,"",1)
                newns=ns.replace(y,"",1)
                newm=int(newms)
                newn=int(newns)
                if newm==0 or newn==0:
                    return (1,1)
                    break
                return (newm,newn)
                break
    else:
        return (1,1) 
        
def nullcancels(values):
    fractions=[]
    for i,n in enumerate(values):
        for m in values[i+1:]:
            frac=float(n)/m
            newfrac=digitcancel(n,m)
            if frac==float(newfrac[0])/newfrac[1] and str(n)[1]!='0':
                fractions.append(newfrac)
    return fractions
    
def reduce(fraction):
    commonfactor=gcd(int(fraction[0]),int(fraction[1]))
    return (fraction[0]/commonfactor,fraction[1]/commonfactor)
    
def productreduceddenom(fractions):
    numer=1
    denom=1
    for f in fractions:
        numer*=f[0]
        denom*=f[1]
    return reduce((numer,denom))

def main():
    start=time.time()
    answer=productreduceddenom(nullcancels(range(10,100)))[1]
    elapsed=time.time()-start
    print answer
    print 'Completed in {elapsed} seconds'.format(elapsed=elapsed)
    return True
    
main()