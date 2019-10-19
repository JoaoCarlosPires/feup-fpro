def mult(M, N):
    res = [[0 for i in range(len(N[0]))] for j in range(len(M))]
    
    if len(N) != len(M[0]):
        return []
    else:
        for c in range(len(N[0])):
            for l in range(len(M)):
                for k in range(len(N)):
                    res[l][c] += M[l][k] * N[k][c]
    return res