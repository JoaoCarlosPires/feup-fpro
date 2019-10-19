def override(l1, l2):
    x = []
    for i in l1:
        verify = 0
        for s in l2:
            if i[0] != s[0]:
                verify += 1
        if verify == len(l2):
            x.append(i)
    for i in l2:
        x.append(i)
    return sorted(x)