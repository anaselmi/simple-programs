def word_funnel(root, target):
    for i, letter in enumerate(root):
        temp = list(root)
        del temp[i]
        temp = "".join(temp)
        print(temp)
        if temp == target:
            return True
    return False

print(word_funnel("reset", "rest"))
