def raise_exception(alist, value):
    to_return = []
    for i in alist:
        try: 
            if i <= value:
                raise ValueError("{0} is not greater than {1}".format(i, value))
        except Exception as excpt:
            to_return.append(excpt)         
    return to_return