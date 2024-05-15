# Write your solution here
def who_won(game_board: list) -> int:
    player_1_count = 0
    player_2_count = 0
    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            if game_board[row][col] == 1:
                player_1_count += 1
            elif game_board[row][col] == 2:
                player_2_count += 1
    if player_1_count > player_2_count:
        return 1
    elif player_2_count > player_1_count:
        return 2
    else:
        return 0
