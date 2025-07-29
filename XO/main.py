def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diags
    ]
    for a,b,c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def tic_tac_toe():
    board = [str(i+1) for i in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter position (1-9): ")
        
        if not move.isdigit() or int(move) not in range(1, 10):
            print("❌ Invalid input. Try again.")
            continue
        
        move = int(move) - 1
        if board[move] in ['X', 'O']:
            print("🚫 Spot taken. Choose another.")
            continue
        
        board[move] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
