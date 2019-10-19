def rm_letter_rev(l, astr):
    new_sentence = ""
    for letter in astr:
        if l == letter:
            continue
        else:
            new_sentence += letter

    final_sentence = new_sentence[::-1]        
        
    return final_sentence
    
