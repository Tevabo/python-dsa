def square_root(n):
    root = n / 2
    for i in range(5):
        root = (1 / 2) * (root + n / root)
    return root


print(square_root(10))
