def player(prev_play, opponent_history=[]):
    # Nếu đối thủ đã chơi ván trước, lưu nước đi vào lịch sử
    if prev_play:
        opponent_history.append(prev_play)
    
    # Nếu đây là ván đầu tiên, chọn 'R' (Rock) làm nước đi ban đầu
    if not opponent_history:
        return "R"
    
    # Đếm tần suất các nước đi của đối thủ trong lịch sử
    counter = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counter[move] += 1
    
    # Dự đoán nước đi tiếp theo của đối thủ bằng cách chọn nước đi phổ biến nhất
    most_common = max(counter, key=counter.get)
    
    # Chọn nước đi để thắng đối thủ
    if most_common == "R":
        return "P"  # Paper thắng Rock
    elif most_common == "P":
        return "S"  # Scissors thắng Paper
    else:
        return "R"  # Rock thắng Scissors
