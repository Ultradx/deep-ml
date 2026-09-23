def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	# return np.array(matrix) * scalar
	for i in range(0, len(matrix)):
		for j in range(0, len(matrix[i])):
			matrix[i][j] *= scalar
	return matrix