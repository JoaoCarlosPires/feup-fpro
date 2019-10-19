def collisions(alist):
    dictionary = {}
    for i in alist:
        sum = 0
        for a in str(i):
            sum += int(a)
        b = sum % 8
        dictionary[b] = 0
    for i in alist:
        sum = 0
        for a in str(i):
            sum += int(a)
        b = sum % 8    
        dictionary[b] += 1
    return dictionary