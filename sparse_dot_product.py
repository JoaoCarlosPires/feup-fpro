def sparse_dot_product(dict1, dict2):
    sum = 0
    for i in dict1:
        for a in dict2:
            if i == a:
                sum += int(dict1[i]) * int(dict2[a])
                
    return sum