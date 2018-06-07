def bubble_sort(values):
    length = len(values) - 1
    if length <= 0:
        # A list with one item is sorted by default.
        return values

    swaps = 0
    for i in range(0, length):
        value = values[i]
        print(i, value)
        next_value = values[i + 1]
        if value > next_value:
            del values[i]
            values.insert(i + 1, value)
            swaps += 1

    if swaps:
        return bubble_sort(values[: -1]) + [values[-1]]
    # If we swap zero times, the entire list is sorted
    else:
        return values

