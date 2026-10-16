def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0: n_negative = n_negative + 1
        return n_negative

#or

def count_negatives1(nums):
    return len([num for num in nums if num < 0])

#or

def count_negatives2(nums):
    return sum([num < 0 for num in nums])

