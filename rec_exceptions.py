def rec_exceptions(l):
    to_return = []
    for i in l:
        try:
            r = i()
            to_return += rec_exceptions(r)
        except Exception as excpt:
            to_return.append(excpt)
    return to_return