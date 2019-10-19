def roman_to_integer(astring):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(len(astring)):
        if i == len(astring)-1:
           sum += roman[astring[i]]
        else:    
            if roman[astring[i]] < roman[astring[i+1]]:
                sum -= roman[astring[i]]
            else:
                    sum += roman[astring[i]]
    return sum