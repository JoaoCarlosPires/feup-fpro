def budgeting2(budget, products, wishlist):
    a = sorted(products, key=products.get, reverse = True)
    for i in a:
        if i in wishlist:
            if products[i] * wishlist[i] <= budget:
                total = products[i] * wishlist[i]
                budget -= total
        
            else:
                c = budget // products[i]
                if c == 0:
                    del wishlist[i]
                    continue
            
                total = products[i] * c
                budget -= total
                wishlist[i] = c
        else:
            continue
    
    return wishlist