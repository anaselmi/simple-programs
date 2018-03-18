def greedybeans(beans, greedies):
    div = 1
    while greedies > 0:
        div += 1
        former_beans = beans
        beans -= beans / div
        greedies -= 1
    return beans
    
checker = [x for x in range(101) if greedybeans(x, 5) == 5]

print(checker)
