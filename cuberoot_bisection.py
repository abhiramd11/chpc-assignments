n = input('Enter the number : ')
epsilon = 0.0000001
high = float(n)
low = 0.0
mid = (low + high) / 2.0

while abs((mid**3)-n) >= epsilon:
	if mid**3 < n:
		low = mid
	else:
		high = mid

	mid = (low + high)/2.0

print "cube root of "+str(n)+"="+str(mid)