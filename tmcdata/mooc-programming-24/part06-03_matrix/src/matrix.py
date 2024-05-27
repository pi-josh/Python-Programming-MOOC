# write your solution here
def matrix_sum():
    """Returns the sum of the elements in the given txt file"""
    matrix_list = combine(read_matrix())
    return sum(matrix_list)


def matrix_max():
    """Returns the element with the greatest value in the given txt file"""
    matrix_list = combine(read_matrix())
    return max(matrix_list)


def row_sums():
    """Returns a list containing the sum of each row in the matrix"""
    matrix_list = read_matrix()
    return [sum(matrix) for matrix in matrix_list]


def read_matrix():
    """Returns a list of row matrices"""
    with open("matrix.txt") as file:
        matrices = []
        for row in file:
            matrix_row = []
            items = row.split(",")
            for item in items:
                matrix_row.append(int(item))
            matrices.append(matrix_row)
    return matrices


def combine(matrices: list) -> list:
    """Returns a list of combined matrices"""
    matrix_list = []
    for matrix in matrices:
        matrix_list += matrix
    
    return matrix_list


if __name__ == "__main__":
    total_sum = matrix_sum()
    largest_num = matrix_max()
    row_sum = row_sums()
    
    print(f"Total sum of the elements in the matrix: {total_sum}")
    print(f"Largest number in the matrix: {largest_num}")
    print(f"Sum of each row in the matrix: {row_sum}")