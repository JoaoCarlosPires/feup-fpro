def flatten(alist):
    final = []
    for a in alist:
        if type(a) == list:
            final += flatten(a)
        else:
            final.append(a)
            
    return final