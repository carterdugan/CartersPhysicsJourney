# vectors are just tuples (x, y, z)

def checkSize(v1, v2):
	if len(v1) != len(v2):
		raise Exception("Vectors do not have the same amount of elements!")

	return len(v1)

def addVectors(v1, v2):
	size = checkSize(v1, v2)
	return tuple(v1[i] + v2[i] for i in range(size))

def scaleVector(scalar, vector):
	return tuple(vector[i] * scalar for i in range(len(vector)))

def dotProduct(v1, v2):
	size = checkSize(v1, v2)
	sum = 0
	for i in range(size): sum += v1[i] * v2[i]
	return sum

def vectorMagnitude(vector):
	return dotProduct(vector, vector)

def determinant(matrix):
	size = checkSize(matrix, matrix[0])
	if(size == 2):
		return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

	sum = 0
	multiplier = 1

	for index, value in enumerate(matrix[0]):

		newMatrix = []

		for j in matrix[1:]:
			ls = []
			newMatrix.append(ls)
			for i, v in enumerate(j):
				if(i != index):
					ls.append(v)

		sum += multiplier * value * determinant(newMatrix)

		multiplier *= -1

	return sum