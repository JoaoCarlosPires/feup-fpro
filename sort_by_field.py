def sort_by_field(filename, field):
    new_list =[]
    with open(filename, "r") as my_file:
        a = my_file.readlines()
        for i in range(1, len(a)):
            abc = []
            for x in a[i].split(","):
                abc.append(x)
            new_list.append(abc)
    b = a[0].split(",")
    
    for i in range(len(b)):
        if field == b[i].strip():
            field = i
    from operator import itemgetter
    c = sorted(new_list, key=itemgetter(field))
    final = ""
    for i in c:
        instance = ""
        for x in range(len(i)):
            if x == len(i)-1:
                instance += i[x]
            else:
                instance += i[x] + ","
        final += instance.strip() + "\n"
    return a[0] + final        