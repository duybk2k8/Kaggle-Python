def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    pass 
    #cách 2: return number < 0
    return True if (number < 0) else False

def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    return not (ketchup or mustard or onion)
    # hàm (ketchup or...) -> chỉ trả true khi ít nhất 1 trong 3 cái true
    # nếu k có cái nào thì mới false => return sẽ true
