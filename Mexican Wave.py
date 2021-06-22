def wave(people):
	return [(people[0:j] + people[j].upper() + people[j+1:]) for j in range(len(people)) if  people[j].isalpha()]

print(wave("hello"))