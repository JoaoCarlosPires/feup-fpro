def triplet(atuple):
    tuples = []
    final_tuples = ()

    for i in atuple:
        for a in atuple:
            if a == i:
                continue
            for x in atuple:
                if x == a or x == i:
                    continue
                else:
                    tuples.append((i,a,x))
                
    for i in tuples:
        if (i[0]+i[1]+i[2]) == 0:
            final_tuples += i
            break

    return final_tuples