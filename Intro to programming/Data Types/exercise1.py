def cost_of_project(engraving, solid_gold):
    value = (not solid_gold) * (50 + 7 * len(engraving)) + solid_gold * (100 + 10 * len(engraving))
    return value

print(cost_of_project("Charlie+Denver", True))
