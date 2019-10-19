def anagrams(alist):
    a1 = []
    j = 0
    
    for i in alist:
        a = list(i.upper())
        j = 0
        for x in a:
            if x == ' ':
                del a[j]
            j += 1    
        a1.append(sorted(a))
    similar = []
        
    for i in range(len(a1)):
        count = 0
        similar_help = []
        for a in range(len(a1)):
            if i == a:
                continue
            if a1[i] == a1[a]:
                count+=1
                similar_help.append(alist[a])
        similar_help.append(alist[i])
        similar.append(sorted(similar_help, key=str.lower))
        j += 1
    similar_final = []
    for i in similar:
        if i not in similar_final:
            similar_final.append(i)
    
    return sorted(similar_final, key=lambda x: x[0].upper())