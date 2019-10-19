def odd_range(start, stop, step):
    a = [x for x in range(start, stop) if x % 2 != 0]
    for i in range(0, len(a), step):
        yield a[i]