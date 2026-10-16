def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends
# nếu n_friends != 0 (ý là có số ở đấy), ví dụ to_smash(90, 4) => lấy 90%4
# nếu n_friends = NONE (k có số), ví dụ n_friends(90) => auto lấy 3 => 90%3
