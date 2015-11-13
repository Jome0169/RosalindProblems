import itertools
Dictionary_of_life = {}
list1 = []
list2 = ''


with open("Example.txt", 'r') as f:
	for line in f:
		if line[0] == '>':
			list1.append(line.rstrip())
		elif (line[0] != '>') and (len(line) == 61):
			list2 += line.rstrip()
		elif (line[0] != '>') and (len(line) != 61):
			list2 += line.rstrip() + '\n'

list3 = list2.split('\n')
#So lets remember the .split() command. Shit is super important and useful for messing with data
#types

def Dictionary(Number1, Number2):
	for item, thing in zip(Number1, Number2):
		total_length = float(len(thing))
		percentagecount = float(0)
		for letter in thing:
			if letter == 'C':
				percentagecount += 1
			elif letter == 'G':
				percentagecount +=1
			else:
				pass
		Percentage = (percentagecount / total_length) * 100
		Dictionary_of_life[item] = Percentage

print Dictionary(list1, list3)
print Dictionary_of_life






