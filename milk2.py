"""
ID: tonyche5
LANG: PYTHON2
TASK: milk2
"""
from operator import itemgetter, attrgetter, methodcaller

#Read the input
fin = open ('milk2.in', 'r')

#Create the output
fout = open ('milk2.out', 'w')

creat_var = locals()

n_worker = int(fin.readline()[0:-1])
all_time_list = []
individual_list = []


for i in range(n_worker):
	begin, end = fin.readline()[0:-1].split()
	begin = int(begin)
	end = int(end)
	all_time_list.append(begin)
	all_time_list.append(end)
	individual_list.append((begin, end))

max_time = max(all_time_list)
min_time = min(all_time_list)

individual_list = sorted(individual_list, key=itemgetter(0))

def is_overlap(a, b):
	a1 = a[1]
	a0 = a[0]
	b0 = b[0]
	b1 = b[1]
	if a0 == b0 and a1 == b1:
		return True
	elif a0 <= b1 and a0 >= b0 and a1 >= b1:
		return True
	elif a0 <= b0 and a1 >= b0 and a1 <= b1:
		return True
	elif a0 >= b0 and a1 <= b1:
		return True
	elif b0 >= a0 and b1 <= a1:
		return True
	else:
		return False

def overlap_exist(individual_list):
	for index, individual in enumerate(individual_list):
		if index > 0:
			if is_overlap(individual_list[index - 1], individual) == True:
				return True
	return False

def generate_new(a, b):
	a1 = a[1]
	a0 = a[0]
	b0 = b[0]
	b1 = b[1]
	new = (min(a0, b0), max(a1, b1))
	return new

def merge_and_remove(individual_list, a, b, new):
	for index, i in enumerate(individual_list):
		if i == a:
			index_a = index
			break
	individual_list.remove(a)
	individual_list.remove(b)
	individual_list.insert(index_a, new)

def clean_overlap(individual_list):
	while overlap_exist(individual_list):
		for index, individual in enumerate(individual_list):
			if index >= 1:
				overlap_result = is_overlap(individual_list[index - 1], individual)
				if overlap_result:
					new = generate_new(individual_list[index - 1], individual)
					merge_and_remove(individual_list, individual_list[index - 1], individual, new)


clean_overlap(individual_list)

###

continuous_true = []
continuous_false = [0]


for index, individual in enumerate(individual_list):
	continuous_true.append(individual[1] - individual[0])
	if index > 0:
		continuous_false.append(individual[0] - individual_list[index - 1][1])

continuous_true = max(continuous_true)
continuous_false = max(continuous_false)


fout.write(("{} {}\n").format(continuous_true, continuous_false))


'''
continuous_true = []
continuous_false = []
cache = individual_list[0][0]

current_overlap = individual_list[0]

if not len(individual_list) <= 1:
	for index, i in enumerate(individual_list):
		if index == 0:
			pass
		elif check_overlap(current_overlap, i) != 0:
			current_overlap = check_overlap(current_overlap, i)
		else:
			continuous_false.append((current_overlap[1], i[0]))
			continuous_true.append((current_overlap[0], current_overlap[1]))
			current_overlap = i
			#print current_overlap[1] - current_overlap[0]
	continuous_true.append((current_overlap[0], current_overlap[1]))
else:	
	continuous_false.append((0,0))
	continuous_true.append((individual_list[0][0], individual_list[0][1]))


#print continuous_true

result = 0
largest_true = None
for i in continuous_true:
	if i[1] - i[0] > result:
		result = i[1] - i[0]
largest_true = i 
  continuous_true = result

result = 0

for i in continuous_false:
	if i[1] - i[0] > result and not (largest_true[0] < i[0] and largest_true[1] > i[1]):
		result = i[1] - i[0]

continuous_false = result

fout.write(("{} {}\n").format(continuous_true, continuous_false))


for worker in individual_list:
	begin = worker[0]
	end = worker[1]
	for index, second in enumerate(periods_list):
		if index + 1 >= begin and index + 1 < end:
			periods_list[index] += 1


#Continuous true
continuous_true = []
current_index = 0
count = 0
while current_index < len(periods_list):
	if current_index == 0 and periods_list[current_index] == 1:
		count += 1
		current_index += 1
	elif periods_list[current_index] == 0:
		continuous_true.append(count)
		count = 0
		current_index += 1
	elif periods_list[current_index] > 0:
		count += 1
		current_index += 1

continuous_true = max(continuous_true)

#Continuous false
continuous_false = []
current_index = min_time - 1
count = 0
while current_index < len(periods_list):
	if current_index == 0 and periods_list[current_index] == 0:
		count += 1
		current_index += 1
	elif periods_list[current_index] > 0 and periods_list[current_index - 1] > 0:
		continuous_false.append(count)
		count = 0
		current_index += 1
	elif periods_list[current_index] == 0:
		count += 1
		current_index += 1
	else:
		current_index += 1

continuous_false = max(continuous_false)
fout.write(("{} {}\n").format(continuous_true, continuous_false))
'''