while True:
    line = input()
    if line == '':
        break
    if line[len(line) - 3:] == '@@@':
        print('', end='')
    elif line[0:2] == '##':
        print(line[2:])
    else:
        print(line)