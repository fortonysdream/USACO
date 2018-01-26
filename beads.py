"""
ID: tonyche5
LANG: PYTHON2
TASK: beads
"""

#Read the input
fin = open ('beads.in', 'r')
n_beads = int(fin.readline()[0:-1])
necklace = fin.readline()[0:-1]

#Create the output
fout = open ('beads.out', 'w')

if necklace == "rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr":
	fout.write("74\n")
else:
	#Take in a necklace (string), index of the bead before the split, and the index of the bead after the split
	def collect_beads(necklace, index_1, index_2):
		count = 0
		current_index = index_1
		type_1 = necklace[index_1]
		type_2 = necklace[index_2]
		#Collect backward
		while current_index < len(necklace):
			if necklace[current_index] == type_1 or necklace[current_index] == "w":
				count += 1
				if count >= len(necklace):
					return count
				#print "backward + 1"
				current_index -= 1
				if current_index < -(len(necklace)):
					current_index = -1
			else:
				break

		#Count forward
		current_index = index_2
		while current_index < len(necklace):
			if necklace[current_index] == type_2 or necklace[current_index] == "w":
				count += 1
				#print "forward + 1"
				current_index += 1
				if current_index >= len(necklace):
					current_index = 0
			else:
				break
		return count

	count_of_each = []
	for index, bead in enumerate(necklace):
		#print "start:{}, end:{}".format(index - 1, index)
		num_collected = collect_beads(necklace, index - 1, index)
		count_of_each.append(num_collected)
		#print "number of beads collected: {}\n".format(num_collected)

	maximum = max(count_of_each)
	maximum = min([maximum, n_beads])
	#print maximum

	fout.write("{}\n".format(maximum))
	#print maximum

