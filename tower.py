# Tower of Hanoi algorithm


def move(n, start, end):
    print("Move disk %i from tower %s to tower %s" % (n, start, end))


def tower(n, start, end, via):
    if n == 1:
        move(n, start, end)
    else:
        tower(n-1, start, via, end)
        move(n, start, end)
        tower(n-1, via, end, start)


tower(4, "A", "C", "B")
