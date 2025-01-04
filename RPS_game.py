import random

def play(player1, player2, num_games, verbose=False):
    outcomes = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    results = {"player1": 0, "player2": 0, "draw": 0}
    
    p1_history = []  # Lịch sử nước đi của player1
    p2_history = []  # Lịch sử nước đi của player2

    for game in range(num_games):
        # Lấy nước đi của player1 và player2
        p1_move = player1("", p2_history) if game == 0 else player1(p2_move, p2_history)
        p2_move = player2("", p1_history) if game == 0 else player2(p1_move, p1_history)

        # Cập nhật lịch sử
        p1_history.append(p1_move)
        p2_history.append(p2_move)

        # Kiểm tra kết quả của ván đấu
        if p1_move == p2_move:
            results["draw"] += 1
        elif (p1_move == "R" and p2_move == "S") or (p1_move == "P" and p2_move == "R") or (p1_move == "S" and p2_move == "P"):
            results["player1"] += 1
        else:
            results["player2"] += 1
        
        if verbose:
            print(f"Game {game + 1}: Player1 ({outcomes[p1_move]}) vs Player2 ({outcomes[p2_move]})")
    
    # In kết quả
    print(f"Results after {num_games} games:")
    print(f"Player1 won {results['player1']} games.")
    print(f"Player2 won {results['player2']} games.")
    print(f"There were {results['draw']} draws.")
