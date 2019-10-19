def find_dtype(atuple, data_type):
    
    new_tuple = ()
    
    for i in range(len(atuple)):
        if type(atuple[i]).__name__ == data_type:
            new_tuple += (atuple[i],)
            
    return new_tuple