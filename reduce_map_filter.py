def reduce_map_filter(args):
    from functools import reduce
    if type(args) != list:
        if args[0] == "map":
            return list(map(args[1], reduce_map_filter(args[2])))
        if args[0] == "filter":
            return list(filter(args[1], reduce_map_filter(args[2])))
        if args[0] == "reduce":
            return reduce(args[1], reduce_map_filter(args[2]))
    else:
        return args