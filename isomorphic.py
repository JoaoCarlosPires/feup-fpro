def isomorphic(astring1, astring2):
    dictionary = {}
    for i in range(len(astring1)):
        dictionary[astring1[i]] = astring2[i]
    for i in dictionary:
        for a in dictionary:
            if i == a:
                continue
            else:
                if dictionary[i] == dictionary[a]:
                    return "'" + astring1 + "' and '" + astring2 +  "' are not isomorphic"
    new_word = ""
    for i in astring1:
        new_word += dictionary[i]
    if new_word == astring2:
        map_tups = []
        for i in dictionary:
            map_tups.append((i,dictionary[i]))
        return "'" + astring1 + "' and '" + astring2 +  "' are isomorphic because we can map: " + str(map_tups)
    else:
        return "'" + astring1 + "' and '" + astring2 +  "' are not isomorphic"