"""
ID: tonyche5
LANG: PYTHON2
TASK: transform
"""

#Read the input
fin = open ('transform.in', 'r')

#Create the output
fout = open ('transform.out', 'w')

n = int(fin.readline()[0:-1])

original_square = []

for n_row in range(n):
	row = fin.readline()[0:-1]
	row_list = []
	for element in row:
		row_list.append(element)
	original_square.append(row_list)

transformed_square = []

for n_row in range(n):
	row = fin.readline()[0:-1]
	row_list = []
	for element in row:
		row_list.append(element)
	transformed_square.append(row_list)


#print original_square
#print transformed_square
def visualize_square(square):
	n = len(square)
	for i in range(n):
		print "{}\n".format(square[i])



def initialize_transformed_square(n):
	transformed_square = []
	for i in range(n):
		transformed_square.append([])
		for j in range(n):
			transformed_square[i].append(0)
	return transformed_square

def ninety_degree_rotation(original_square, n):
	transformed_square = initialize_transformed_square(n)

	for x_old in range(n):
		for y_old in range(n):
			x_new = y_old
			y_new = n - 1 - x_old

			transformed_square[x_new][y_new] = original_square[x_old][y_old]

	return transformed_square



#print ninety_degree_rotation(original_square, n)

def one_eighty_degree_rotation(original_square, n):
	transformed_square = ninety_degree_rotation(original_square, n)
	transformed_square = ninety_degree_rotation(transformed_square, n)

	return transformed_square 

def two_seventy_degree_rotation(original_square, n):
	transformed_square = one_eighty_degree_rotation(original_square, n)
	transformed_square = ninety_degree_rotation(transformed_square, n)

	return transformed_square

def reflection(original_square, n):
	transformed_square = initialize_transformed_square(n)

	for x_old in range(n):
		for y_old in range(n):
			x_new = x_old
			y_new = n - 1 - y_old

			transformed_square[x_new][y_new] = original_square[x_old][y_old]

	return transformed_square


def classification(original_square, transformed_square, n):
	reflection_transformation = reflection(original_square, n)
	if ninety_degree_rotation(original_square, n) == transformed_square:
		return 1
	elif one_eighty_degree_rotation(original_square, n) == transformed_square:
		return 2
	elif two_seventy_degree_rotation(original_square, n) == transformed_square:
		return 3
	elif reflection_transformation == transformed_square:
		return 4
	elif transformed_square in [ninety_degree_rotation(reflection_transformation, n), one_eighty_degree_rotation(reflection_transformation, n), two_seventy_degree_rotation(reflection_transformation, n)]:
		return 5
	elif original_square == transformed_square:
		return 6
	else:
		return 7

result = classification(original_square, transformed_square, n)


fout.write("{}\n".format(result))

