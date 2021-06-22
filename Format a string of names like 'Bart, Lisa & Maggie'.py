#import unittest as test

def namelist(names):
	if len(names) == 0: return ''
	arr = [dic[i] for dic in names for i in dic]
	n = arr.pop(len(arr) - 1)
	return ', '.join(arr) + ((' & ' + n) if len(names) > 1 else n)

	#arr = [dic[i] for dic in names for i in dic]
	
	
arr0 = []
arr1 = [{'name': 'Bart'}]
arr2 = [{'name': 'Bart'},{'name': 'Lisa'}]
arr = [{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]
print(namelist(arr))
#namelist(eval(arr3))