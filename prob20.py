fact=1
for i in range(1,101):
	fact=fact*i
digits=str(fact)
sum=0
for i in digits:
	sum=sum+int(i)
print sum
