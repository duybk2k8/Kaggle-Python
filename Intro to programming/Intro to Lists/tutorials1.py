flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(len(flowers_list))

#index
print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])
print("Last entry:", flowers_list[9])

# pull first x entries: [:x]
# pull last y entries: [-y:]
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

#remove items
flowers_list.remove("globe thistle")
print(flowers_list)

#add items
flowers_list.append("snapdragon")
print(flowers_list)