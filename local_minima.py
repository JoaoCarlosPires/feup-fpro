def local_minima(alist, n):
    count1 = 0
    count2 = 0
    final = []
    
    for i in range(1, int(((n-1)/2)+1)):
        if alist[0] <= alist[i]:
            count1 += 1

    if count1 == int(((n-1)/2)):
        final.append((alist[0], 0))
    
    if len(alist) != 2:    
        for i in range(1, len(alist)-1):
            count = 0
            
            for a in range(i, int(i+((n-1)/2))+1):
                if i ==a:
                    continue
                if alist[i] <= alist[a]:
                    count += 1  
        
            for x in range(int(i-((n-1)/2)), i):
                if x == i:
                    continue
                if alist[i] <= alist[x]:
                    count += 1
        
            if count == int(n-1):
                final.append((alist[i], i))
    
        for i in range(len(alist)-int((n-1)/2), len(alist)):
            if alist[len(alist)-1] <= alist[i]:
                count2 += 1
    
        if count2 == int(((n-1)/2)):
            final.append((alist[len(alist)-1], len(alist)-1))
    
    else:
        
        for i in range(len(alist)-int((n-1)/2), len(alist)):
            if alist[len(alist)-1] <= alist[i]:
                count2 += 1
    
        if count2 == int(((n-1)/2)):
            final.append((alist[len(alist)-1], len(alist)-1))
    
    ultimate = []
        
    for i in range(len(final)):
        if int(final[i][1])-1 != int(final[i-1][1]):
            ultimate.append(final[i])
            
    return ultimate