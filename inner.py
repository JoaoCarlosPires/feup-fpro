def inner(u, v):
    sol = 0
    for i in range(len(u)):
        a = u[i] * v[i]
        sol += a
    return sol