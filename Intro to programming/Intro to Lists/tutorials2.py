hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Length of the list:", len(hardcover_sales))
print("Entry at index 2:", hardcover_sales[2])

#min max
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

#sum
print("Total books sold in one week:", sum(hardcover_sales))
print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)