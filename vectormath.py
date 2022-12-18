'''

This small library of vector functions serves one purpose and one
purpose only: To help me practice my python/programming skills and to
provide me with a simple set of tools for performing vector math.

The code is not meant to be be good. It is not meant to be fast or
efficient, or even easy to read to anyone other than myself. So if
you happen to come across this code and have a problem with it, please
keep that to yourself.

Thanks.
  - CD

'''

def checkEqualSize(v1, v2):
	if len(v1) != len(v2):
		raise Exception("Vectors do not have the same amount of elements!")

	return len(v1)

def addVectors(v1, v2):
	size = checkEqualSize(v1, v2)
	return tuple(v1[i] + v2[i] for i in range(size))

def scaleVector(scalar, vector):
	return tuple(vector[i] * scalar for i in range(len(vector)))

def dotProduct(v1, v2):
	size = checkEqualSize(v1, v2)

	# s means sum. stupid reserve
	s = 0
	for i in range(size): s += v1[i] * v2[i]
	return s

def vectorMagnitude(vector):
	return dotProduct(vector, vector)

def determinant(matrix):
	size = checkEqualSize(matrix, matrix[0])

	# edge case
	if(size == 2):
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


	s = 0
	multiplier = 1

	for index, value in enumerate(matrix[0]):

		newMatrix = []

		for j in matrix[1:]:
			ls = []
			newMatrix.append(ls)
			for i, v in enumerate(j):
				if(i != index):
					ls.append(v)

		s += multiplier * value * determinant(newMatrix)

		multiplier *= -1

	return s