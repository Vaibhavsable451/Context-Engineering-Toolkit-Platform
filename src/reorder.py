def lost_in_middle(items_sorted_best_first):
    """Place the strongest items at the beginning and end; weakest in the middle."""
    front, back = [], []
    for i, it in enumerate(items_sorted_best_first):
        (front if i % 2 == 0 else back).append(it)
    return front + back[::-1]
