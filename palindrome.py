def palindrome(astring):
    
    astring_lenght = len(astring)
    number_substrings = 0
    
    for i in range(astring_lenght + 1):
        verification = 1
        while (i + verification) <= astring_lenght:
            substring = astring[i:i+verification]
            if (substring == substring[::-1]) and (len(substring) != 1):
                number_substrings += 1
            verification += 1
    
    user_output = "For string '{0}': {1} palindrome substrings".format(astring, number_substrings)
    return user_output    