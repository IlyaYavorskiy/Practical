class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, i)) for i in self.matrix)

    def __add__(self, other):

        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                  for i in range(len(self.matrix))]
        return result

        # result = [[self.matrix[i][j] + other.matrix[i][j] for i in range(len(self.matrix))]
        #           for j in range(len(self.matrix[0]))]
        # return [*zip(*result)]

# --------------------------------------------------------------------------------------------
#         result = [
#             [0, 0],
#             [0, 0],
#             [0, 0]
#         ]
#
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[0])):
#                 result[i][j] = self.matrix[i][j] + other.matrix[i][j]
#         return result


# result = [
#     [0, 0],
#     [0, 0],
#     [0, 0]
# ]

# --------------------------------------------------------------------------------------------

m1 = Matrix([
    [1, 2],
    [3, 4],
    [5, 6]
])
m2 = Matrix([
    [7, 8],
    [9, 10],
    [11, 12]
])
m3 = Matrix(m1 + m2)
print(m1)
print(m2)
print(m3)
