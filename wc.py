def wc(filename):
    lines = 0
    words = 0
    car = 0
    with open(filename, "r") as my_new_handle:
        for the_line in my_new_handle:
            lines += 1
            words += len(the_line.split())
            for word in the_line:
                for i in word:
                    car += 1
    return (lines, words, car)