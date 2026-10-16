#EXERCISE 2:
def elementwise_greater_than(L, thresh):
    res = []
    for ele in L:
        res.append(ele > thresh)
    return res

#or

def elementwise_greater_than(L, thresh):
    return [ele > thresh for ele in L]

#EXERCISE 1
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    count = 0 # phải đặt ngoài for, k thì mỗi lúc nó xong nó lại reset về 1
    for num in nums:
        if num % 7 == 0:
            count += 1
    if count > 0:
        return True
    else:
        return False
    
#câu sai
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True #return là nó thoát luôn k xét đến phần tử sau nữa
        else:
            return False
        
#cách khác
def has_lucky_number(nums):
    for num in nums:
        if num % 7 == 0:
            return True
    return False

#or 

def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])
#any sẽ return true nếu trong bool(x) có 1 cái true, nếu k tự động về false

#EXERCISE 3:
def menu_is_boring(meals):
    for i in range(len(meals) - 1): # bỏ qua cái cuối
        if meals[i] == meals[i + 1]:
            return True
    return False

for i in range(5):
    print(i)