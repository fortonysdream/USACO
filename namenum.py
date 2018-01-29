"""
ID: tonyche5
LANG: PYTHON2
TASK: namenum
"""
import string

#Read the input
fin = open ('namenum.in', 'r')

#Create the output
fout = open ('namenum.out', 'w')

name_dict = open ('dict.txt', 'r')

name_list = []

current = "1"
while current != "":
	current = name_dict.readline()[0:-1]
	name_list.append(current)

serial = fin.readline()[0:-1]
serial_list = []

for i in serial:
	serial_list.append(int(i))

alphabet_list = list(string.ascii_uppercase)
alphabet_list.remove("Q")
alphabet_list.remove("Z")
alphabet_dict = {}

for i in range(2, 10):
	alphabet_dict[i] = alphabet_list[(i - 2) * 3 : (i - 2) * 3 + 3]

alphabets_for_serial = []

for i in serial_list:
	alphabets_for_serial.append(alphabet_dict[i])

possible_names = []

n_alphabets = len(serial)

current_position_list = []

for i in range(n_alphabets):
	current_position_list.append(0)

'''
def up_date_position(current_position_list):
	current_position_list[n_alphabets - 1] += 1
	while 3 in current_position_list:
		for index, i in enumerate(current_position_list):
			if i == 3:
				current_position_list[index] = 0
				current_position_list[index - 1] += 1
'''

name_list_reduced = [i for i in name_list if len(i) == n_alphabets]
final_names = []

for possible_name in name_list_reduced:
	is_final = True
	for i in range(n_alphabets):
		if possible_name[i] not in alphabets_for_serial[i]:
			is_final = False
	if is_final:
		final_names.append(possible_name)

'''
while current_position_list != [2] * n_alphabets:
	#current = []
	for index, nth in enumerate(alphabets_for_serial):
		#current.append(nth[current_position_list[index]])
		#possible_names.append("".join(current))
		up_date_position(current_position_list)





for j in range(n_alphabets):
	name_list_reduced = [i for i in name_list_reduced if i[j] in alphabets_for_serial[j]]

final_names = [i for i in possible_names if i in name_list_reduced]

'''

if len(final_names) == 0:
	fout.write("NONE\n")
else:
	for i in final_names:
		fout.write("{}\n".format(i))

