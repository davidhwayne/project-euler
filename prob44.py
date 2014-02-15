from math import sqrt

done=False
dif=0
low=0
up=0
i=2
while not done:
	m=(i*(3*i-1))/2
	j=i-1
	while j>0:
		n=(j*(3*j-1))/2
		f=(1+sqrt(1+24*(m-n)))/6
		g=(1+sqrt(1+24*(m+n)))/6
		if int(f)==f and int(g)==g:
			up=i
			low=j
			dif=m-n
			done=True
			break
		j=j-1
	i+=1
print low
print up
print dif
