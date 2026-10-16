#exercise 2
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

#exercise 4
a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# first being the length of a, the second being the length of b and so on.
lengths = [3, 2, 0, 2]
#b thì [2,3] dc coi là 1
#d thì nó chỉ là [2, 3]

#exercise 5
def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if (arrivals.index(name) >= (len(arrivals))/2) and (name != arrivals[-1]) : return True
    else: return False