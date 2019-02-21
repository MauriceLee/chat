def read_file(filename):
    chat = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            chat.append(line.strip())
    print(chat)
    return chat

def write_file(filename, output):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for out in output:
            f.write(out + '\n')

def main():
    chat = read_file('input.txt')
    output = []
    who = 0
    for line in chat:
        if 'Allen' in line:
            who = 1
            continue
        elif 'Tom' in line:
            who = 2
            continue
        elif who == 1:
            output.append('Allen: ' + line)
        else:
            output.append('Tom: ' + line)
    print(output)
    write_file('output.txt', output)

main()