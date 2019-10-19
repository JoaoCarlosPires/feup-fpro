def manipulator(l, cmds):
    final_string = ""
    for i in cmds:
        if "insert" in i:
            a = i.split()
            b = int(a[1])
            c = int(a[2])
            l.insert(b,c)
        elif i == "print":
            final_string += str(l) + " "
        elif "remove" in i:
            for a in range(len(l)):
                if int(i[7:]) in l:
                    del l[a]
        elif "append" in i:
            l.append(int(i[7:]))
        elif i == "sort":
            l = sorted(l)
        elif i == "pop":
            l.pop()
        elif i == "reverse":
            l = l[::-1]
    return final_string