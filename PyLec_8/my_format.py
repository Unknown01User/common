def my_format(string, *argv):
    index = 0
    numbers = []
    while index < len(string):
        if string[index] == '{':
            index += 1
            if not index < len(string):
                break
            number = ''
            while string[index].isdigit():
                number += string[index]
                index += 1
                if not index < len(string):
                    break
            if index < len(string) and string[index] == '}':
                numbers.append(int(number))
        index += 1
    if max(numbers) >= len(argv):
        print(f"incorrect index {{{max(numbers)}}} in '{string}'")
        return None
    for number in numbers:
        string = string.replace(f"{{{numbers[number]}}}", str(argv[number]))
        # print(string)
    return string


if __name__ == "__main__":
    string = ' sdfdf {10} saf {23'
    print(my_format(string, 23, 'some'))
