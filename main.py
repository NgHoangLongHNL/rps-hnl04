from RPS_game import play
from RPS import player  # Đảm bảo bạn đã nhập đúng hàm player từ RPS.py

# Tạo các bot đối thủ khác nhau (bạn cần phải tự định nghĩa các bot này trong RPS_game.py hoặc import từ nơi khác)
# Ví dụ về các bot đối thủ (những bot này có thể thay đổi tùy thuộc vào yêu cầu của bạn):

# Bot quincy
def quincy(prev_play, opponent_history=[]):
    return "R"  # Bot này chơi "Rock" liên tục

# Bot abigail
def abigail(prev_play, opponent_history=[]):
    return "P"  # Bot này chơi "Paper" liên tục

# Bot random_player
import random
def random_player(prev_play, opponent_history=[]):
    return random.choice(["R", "P", "S"])  # Bot này chơi ngẫu nhiên

# Bot mr_robot (một chiến lược đơn giản)
def mr_robot(prev_play, opponent_history=[]):
    if prev_play == "R":
        return "S"  # Nếu đối thủ chọn "Rock", bot này chơi "Scissors"
    elif prev_play == "P":
        return "R"  # Nếu đối thủ chọn "Paper", bot này chơi "Rock"
    else:
        return "P"  # Nếu đối thủ chọn "Scissors", bot này chơi "Paper"

# Chạy thử 1000 ván đấu với các bot đối thủ
print("Chơi với Bot Quincy:")
play(player, quincy, 1000, verbose=True)

print("\nChơi với Bot Abigail:")
play(player, abigail, 1000, verbose=True)

print("\nChơi với Bot Random Player:")
play(player, random_player, 1000, verbose=True)

print("\nChơi với Bot Mr Robot:")
play(player, mr_robot, 1000, verbose=True)
