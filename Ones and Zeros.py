def binary_array_to_number(arr):
	return(sum([value * 2 ** offset  for (offset, value) in enumerate(arr[::-1])]))
	# return int("".join(map(str, arr)), 2)

#binary_array_to_number('spam')
binary_array_to_number([0, 0, 1, 0])