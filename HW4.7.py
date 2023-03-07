#HW 4.7(Tuples)


def Project_1():
	test_tup = (15, 20, 123, 47, 26, 81)
	n = 0
	total = 0

	while n < len(test_tup):
		total += test_tup[n]
		n += 1
	
	print(f'The total of the tuple is {total}.')

	return Project_1


def Project_2():
	test_tup = (15, 20, 123, 47, 26, 81)
	print(f'The largest number of the tuple is {max(test_tup)}.')

	return Project_2


def Project_3():
	test_tup = ([17, 28], [93, 11], [20, 17])

	print(f'The total of element 0 of the tuple is {sum(test_tup[0])}.')
	print(f'The total of element 1 of the tuple is {sum(test_tup[1])}.')
	print(f'The total of element 2 of the tuple is {sum(test_tup[2])}.')

	print(sum(test_tup[0]) + sum(test_tup[1]) + sum(test_tup[2]))

	return Project_3


def Project_4():
	input_tup = ([2, 20], [44, 1], [3, 13])
	print(sorted(input_tup, key=sum))

	return Project_4

