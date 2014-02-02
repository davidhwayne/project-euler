count=0
day=6
for year in range(1,101):
	for month in range(1,13):
		if month==4 or month==6 or month==9 or month==11:
			while day<=30:
				day=day+7
			day=day%30
		elif month==2:
			if year%4==0:
				while day<=29:
					day=day+7
				day=day%29
			else:
				while day<=28:
					day=day+7
				day=day%28
		else:
			while day<=31:
				day=day+7
			day=day%31
		if day==1:
			count=count+1
			
print count


