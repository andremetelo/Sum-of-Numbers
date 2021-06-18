#!/usr/bin/python3
import sys
from pandas.core.common import flatten

def removeduplicates(x):
  return list(dict.fromkeys(x))


#list_of_numbers = [1,2,3,4]
#Setsup numbers from CLI command
list_of_numbers = []
for item in range(1,len(sys.argv)):
	list_of_numbers.append(int(sys.argv[item]))

print("List of Numbers:")
print(*list_of_numbers)

count = len(list_of_numbers)

#Creates the single item in the list as seed for new solutions. From there dynamic program assembles all other lists
results = []
results.append([list_of_numbers[0]])

#This will add all the lists of itens with the following numbers
for n in range(1, count):
	new_entries=[]
	new_entries.append([list_of_numbers[n]])
	for result in results:
		temp = []
		temp.append(result)
		temp.append(list_of_numbers[n])
		new_entries.append(temp)

	results.extend(new_entries)
	del new_entries[:] #No longer need to use memory for the last cycle
#print (*results)	
#Results had several levels of lists, Thus the next step

#Flatten Lists to have a single level of the list:
flat= []
for item in results:
	flat.append(list(flatten(item)))
del results[:] #No longer need the messy list

#Sums all the numbers
sums = []
for item in flat:
	sums.append(sum(item))

sums.sort()
print("Sums:")
del flat[:]

sums = removeduplicates(sums)

print(*sums)
