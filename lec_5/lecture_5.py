def max_(*args):
    if args:
        max_value = args[0]
        for item in args[1:]:
            if item > max_value:
                max_value = item
        return max_value
    """Second variant"""
    #     return sorted(args)[-1]
    return None


def enumerate_(a):
    index = 0
    for item in a:
        yield index, item
        index += 1


print(max_(12, 42, 6, 35))
for i in enumerate_([12, 42, 6, 35]):
    print(i)
