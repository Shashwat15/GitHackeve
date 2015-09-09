def bin_to_dec(s):
	lis = list(s)
	lis.reverse()
	outlis = []
	i=0
	sum = 0
	for dig in lis:
		digit = int(dig)
		curNum = digit*(2**i)
		sum+=curNum	
		i+=1
	return sum
	
num = "101"
print(bin_to_dec(num))