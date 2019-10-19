def budgeting(budget, products, wishlist):
    total = 0
    for i in wishlist:
        total += wishlist[i] * products[i]
    if total <= budget:
        return wishlist
    else:
        total = 0
        a = sorted(products, key=products.get, reverse = True)
        print(a)
        for i in a:
            if budget <= 0:
                del wishlist[i]
                break
            elif i in wishlist:
                if products[i] * wishlist[i] <= budget:
                    total = products[i] * wishlist[i]
                    budget -= total
                else:
                    c = budget // products[i]
                    if c == 0:
                        del wishlist[i]
                        break
                    total = products[i] * c
                    budget -= total
                    wishlist[i] = c
               
        return wishlist