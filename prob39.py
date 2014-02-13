from math import sqrt

highest=0
current=0
for i in range(1001):
	count=0
	for j in range(1,(int(sqrt(i))+1)/4):
		for k in range(j+1,(int(sqrt(i))+1)/4):
			n=1
			while n*(2*k**2+2*k*j)<i:
				n+=1
			if n*(2*k**2+2*k*j)==i:
				count=count+1
	if count>highest:
		highest=count
		current=i
print highest
print current
				

