def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    return (ketchup + mustard + onion == 1)
# k cần int(ketchup), add boolean nó sẽ tự converse