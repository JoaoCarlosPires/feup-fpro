def calculator(expr): 
    if type(expr) != tuple:
        return expr       
    l = calculator(expr[0])
    r = calculator(expr[2])
    operator = expr[1]
    
    return eval(str(l)+operator+str(r))