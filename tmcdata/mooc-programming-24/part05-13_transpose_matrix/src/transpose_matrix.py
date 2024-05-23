# Write your solution here
def transpose(matrix: list):
    temp_matrix = []
    for row in matrix:
        temp_matrix.append(row[:])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = temp_matrix[j][i]
    

def print_matrix(matrix: list):
    for row in matrix:
        for column in row:
            print(column, end=" ")
        print()
    print()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    transpose(matrix)
    print_matrix(matrix)