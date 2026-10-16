def get_expected_cost(beds, baths, has_basement):
    value = 80000 + beds * 30000 + baths * 10000 + has_basement * 40000
    return value
print(get_expected_cost(1,1,False))