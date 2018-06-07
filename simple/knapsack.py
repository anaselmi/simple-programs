from operator import itemgetter
#[0] is weight, [1] is value
test = [[12, 4], [2, 2], [1, 1], [4, 10], [1, 2]]

class Knapsack:
    pass

def knapsack(items, limit):
    items = items[:]
    for item in items:
        value_per_weight = item[1] / item[0]
        item.insert(0, value_per_weight)
    items = sorted(items, key=itemgetter(0))[::-1]
    knapsack = []
    knapsack_weight = 0
    knapsack_value = 0
    for item in items:
        while knapsack_weight + item[1] < limit:
            knapsack.append(item)
            knapsack_weight += item[1]
            knapsack_value += item[2]
    return "The knapsack weights %d units, is worth %d value, has %d items and has %s inside it" %(knapsack_weight, knapsack_value, len(knapsack), knapsack)

print(knapsack(test, 15))





