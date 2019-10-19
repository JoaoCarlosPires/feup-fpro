def soup(matrix, word):
    lister = []
    dicionario = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H",
                  8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
                  16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "X", 23: "W", 24: "Y", 25: "Z"} 
    l = len(matrix)
    c = len(matrix[0])
    if len(word) == 1:
        for a in range(l):
            for b in range(c):
                if matrix[a][b] == word:
                    return str(a) + str(b) 
    else:
        for a in range(l):
            for b in range(c):
                if matrix[a][b] == word[0]:
                    lister.append(str(a)+str(b))
                    lister += soup(matrix, word[1:])
    
    return dicionario[int(lister[0][0])]+str(int(lister[0][1]) +1)    