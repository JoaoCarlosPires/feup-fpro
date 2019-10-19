def formal(name):

    words = name.split()
    i = len(words)

    first_letters = [word[0] for word in words]
    final_name = str(words[i-1]) + ", "

    for a in range(i-1):
        final_name += str(first_letters[a]) + ". "
    
    return final_name