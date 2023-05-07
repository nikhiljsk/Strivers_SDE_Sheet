# Approach 1
# Used for n point to n point distance, DAG
# O(N3), O(N2)
class Solution:
	def shortest_distance(self, matrix):
		n = len(matrix)

		for i in range(n):
			for j in range(n):
				if matrix[i][j] == -1:
					matrix[i][j] = int(1e8)
			if i==j:
				matrix[i][j] == 0

		for via in range(n):
			for i in range(n):
				for j in range(n):
					matrix[i][j] = min(matrix[i][j], matrix[i][via]+matrix[via][j])

        # To check if graph has negative cycle
        # for i in range(n):
        #     if matrix[i][i] < 0:
        #     return True

		for i in range(n):
			for j in range(n):
				if matrix[i][j] == int(1e8):
					matrix[i][j] = -1