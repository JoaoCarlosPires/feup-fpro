def translate(astring, table):

    newstring = ""

    for i in astring:
        j = 0
        count = 0
        while j < len(table):
            if table[j][0] == i:
                count += 1
                newstring += str(table[j][1])
                break
            j += 1
        
        if count == 0:
            newstring += str(i)
                
    return newstring