def ducci(*args):
    return [abs(n - args[0]) if i == len(args) - 1
            else abs(n - args[i + 1])
            for i, n in enumerate(args)]


def ducci_steps(*args):
    # The original ducci sequence is the first step.
    steps = 1
    sequence = [list(args)]
    while True:
        steps += 1
        new = ducci(*sequence[-1])
        sequence.append(new)
        if all(x == 0 for x in new):
            return steps
        if new in sequence[:-1]:
            # If we repeat ducci sequences, we return steps at the second
            # instance, not the first.
            return steps
