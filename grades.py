def medias(records):
 
    soma = 0
    num = 0
    for a in records[2]:
        soma += a
        num += 1
    medias = soma/num
    return medias

def sort_grades(records):
    
    names = sorted(records)
    by_order_records = tuple(sorted(names, key=medias, reverse = True))
    return by_order_records