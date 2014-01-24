sum=2
m=1
n=2
for i in range(4000000):
	n,m=n+m,n
	if n%2==0 and n<4000000:
		sum=sum+n
	elif n>=4000000:
		break

print sum
