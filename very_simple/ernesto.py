def ernesto(end):
    switch = 1
    n = 0
    out = 0
    sent = ""

    while True:
        n += 1
        if switch:
            out += n
            switch = 0
            sent += "+ %d "% (n)
        else:
            out -= n
            switch = 1
            sent += "- %d "% (n)

        if n == end:
            sent = sent[2:] + "= %d"% (out)
            return sent
            break

print(ernesto(4))



        