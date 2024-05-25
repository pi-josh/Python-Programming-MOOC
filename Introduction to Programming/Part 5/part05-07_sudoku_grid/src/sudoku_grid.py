# Write your solution here
def row_correct(sudoku: list, row_no):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True


def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True


def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    numbers = []
    for row in range(row_no, row_no+3):
        for col in range(column_no, column_no+3):
            number = sudoku[row][col]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(len(sudoku)):
        is_row_correct = row_correct(sudoku, i)
        for j in range(len(sudoku[i])):
            is_column_correct = column_correct(sudoku, j)
            if i % 3 == 0 and j % 3 == 0:
                is_block_correct = block_correct(sudoku, i, j)
            if not (is_row_correct and is_column_correct and is_block_correct):
                return False
    return True


def main():
    sudoku = [
    [ 2, 0, 1, 9, 8, 0, 4, 0, 3 ],
    [ 8, 0, 0, 6, 3, 0, 0, 0, 0 ],
    [ 6, 4, 3, 0, 0, 0, 5, 9, 8 ],
    [ 3, 1, 6, 7, 5, 0, 0, 4, 0 ],
    [ 8, 4, 9, 3, 1, 6, 0, 7, 0 ],
    [ 0, 0, 0, 8, 4, 9, 0, 3, 0 ],
    [ 1, 0, 3, 0, 0, 0, 0, 4, 6 ],
    [ 5, 9, 7, 4, 0, 0, 3, 1, 2 ],
    [ 4, 6, 8, 1, 2, 0, 7, 0, 0 ],
    ]
    print(sudoku_grid_correct(sudoku))


if __name__ == "__main__":
    main()