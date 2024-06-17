import numpy as np

class LinearAlgebra:
    def __init__(self) -> None:
        pass
    def printMatrix(self, matrix):
        print(matrix)
    def checkShapeAdd(self, matrix1, matrix2):
        return matrix1.shape == matrix2.shape
    def checkShapeMultiply(self, matrix1, matrix2):
        return matrix1.shape[1] == matrix2.shape[0]
    def matrixSummation(self, matrix1, matrix2):
        if self.checkShapeAdd(matrix1, matrix2):
            board = np.zeros(matrix1.shape)
            for i in range(len(matrix1)):
                for j in range(len(matrix1[i])):
                    board[i][j] = matrix1[i][j] + matrix2[i][j]
            return board
        else:
            return "The shapes of the matrices are not the same"
    def matrixMultiplication(self, matrix1, matrix2):
        if self.checkShapeMultiply(matrix1, matrix2):
            board = np.zeros((matrix1.shape[0],matrix2.shape[1]))
            for i in range(matrix1.shape[0]):
                for j in range(matrix2.shape[1]):
                    board[i][j] = sum([matrix1[i][k]*matrix2[k][j] for k in range(matrix1.shape[1])])
            return board



#LinearAlgebra().printMatrix(np.array([[1, 2], [3, 4]]))
#print(LinearAlgebra().matrixSummation(np.array([[1, 2], [3, 4]]), np.array([[1, 2], [3, 4]])))
#print(LinearAlgebra().matrixMultiplication(np.ones((4,3)),np.ones((3,2))))
print(LinearAlgebra().matrixMultiplication(np.array([[1,0,0],[0,1,0],[0,0,1]]),np.array([[1,2,-1],[3,1,4],[2,3,1]])))
#print(LinearAlgebra().matrixMultiplication(np.array([[1,2],[2,4]]),np.array([[2,1],[3,2]])))
