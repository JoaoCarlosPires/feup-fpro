def cut(filename, delimiter, field):
    if type(field) == int:
        field = [field]
    final = ""
    with open(filename, "r") as myfile:
        for the_line in myfile:
            a = the_line.strip().split(delimiter)

            for i in field:
                final += str(a[i-1])
                final += delimiter
            final = final[:-len(delimiter)]
            final += "\n"
    return final