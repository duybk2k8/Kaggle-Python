def blackjack_hand_greater_than(hand_1, hand_2):

    result_1 = 0
    count_1 = 0
    result_2 = 0
    count_2 = 0
    for i in hand_1:
        if(i.isdigit() == True): result_1 += int(i)
        elif i == 'A': 
            result_1 += 11 
            count_1 += 1
        else: result_1 += 10 
    
    while result_1 > 21 and count_1 > 0:
        result_1 -= 10
        count_1 -= 1
    
    for i in hand_2:
        if(i.isdigit() == True): result_2 += int(i)
        elif i == 'A': 
            result_2 += 11 
            count_2 += 1
        else: result_2 += 10 
    
    while result_2 > 21 and count_2 > 0:
        result_2 -= 10
        count_2 -= 1
    
    if result_1 > result_2 and result_1 <= 21 and result_2 <= 21: return True
    elif result_2 > 21 and result_1 < 21: return True
    else: return False

print(blackjack_hand_greater_than(['J', 'A', 'A', '2'], ['9', '6', 'K', 'A', '5', 'J']))
