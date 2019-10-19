def exception_str(f):
    try: 
        f()
        return "No exception was raised"
    except Exception as str_to_return:
        return str(str_to_return)