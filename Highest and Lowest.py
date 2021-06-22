def high_and_low(numbers):
	l = list(map(int, numbers.split(' ')))
	return str(max(l)) + ' ' + str(min(l))
	#return "{} {}".format(max(n), min(n))
	  #return f"{max(numbers)} {min(numbers)}"

print(high_and_low("1 2 -3 4 5"))