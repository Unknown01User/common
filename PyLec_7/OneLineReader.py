def one_line_reader(file_name):
    with open(file_name, 'r') as f:
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                break


for line in one_line_reader("test.txt"):
    print(line)
