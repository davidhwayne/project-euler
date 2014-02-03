fibnums=[1,1]
index=2
while len(str(fibnums[-1]))<1000:
	fibnums.append(fibnums[-2]+fibnums[-1])
	index+=1
print index
