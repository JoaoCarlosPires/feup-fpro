def count(word, phrase):
    
    count = 0
    new_phrase = phrase.split()
    for words in new_phrase:
        if (word.upper() == words.upper()):
            count += 1
            continue            
    
    return count