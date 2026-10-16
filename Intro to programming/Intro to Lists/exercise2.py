test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)


def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])
