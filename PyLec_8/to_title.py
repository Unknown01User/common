def to_title(string):
    first_char = True
    gap = False
    res = []
    for char in string:
        if char == ' ':
            gap = True
            res.append(char)
        elif char.isalpha():
            if first_char:
                res.append(char.upper())
                first_char = False
                gap = False
            elif gap:
                res.append((char.upper()))
                gap = False
            else:
                res.append(char)
    return "".join(res)


if __name__ == "__main__":
    a = "   aaaa  aaa aaa a"
    b = "bbb b bbbb bb    "
    c = "   ccc   c  c   cc    "
    print(a.title() == to_title(a))
    print(b.title() == to_title(b))
    print(c.title() == to_title(c))
    print(to_title(a))
    print(to_title(b))
    print(to_title(c))
