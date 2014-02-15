found=False
next=0
i=143
j=165
k=285
while not found:
	i=i+1
	num=i*(2*i-1)
	while (j*(3*j-1))/2<num:
		j=j+1
	while (k*(k+1))/2<num:
		k=k+1
	if (j*(3*j-1))/2==num and (k*(k+1))/2==num:
		found=True
		next=num
print next
		

