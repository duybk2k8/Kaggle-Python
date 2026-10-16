


def estimate_average_slot_payout(n_runs):
    """Run the slot machine n_runs times and return the average net profit per run.
    Example calls (note that return value is nondeterministic!):
    >>> estimate_average_slot_payout(1)
    -1
    >>> estimate_average_slot_payout(1)
    0.5
    """
    count = 0
    #for i in range(n_runs):
        #count += (play_slot_machine() - 1)
    return (count)/n_runs
print(estimate_average_slot_payout(10000000))

