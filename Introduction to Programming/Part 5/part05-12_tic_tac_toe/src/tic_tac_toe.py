# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if x > 2 or x < 0 or y > 2 or y < 0:
        return False
    elif game_board[y][x]:
        return False
    game_board[y][x] = piece
    return True


if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn([['X', '', 'O'], ['', 'O', 'O'], ['O', '', '']], 2, -1, "X"))
    print(game_board)