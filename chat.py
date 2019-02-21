def read_file(filename):
    chat = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    print(chat)
    return chat

def convert(chat):
    output = []
    person = None
    for line in chat:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            output.append(person + ': ' + line)
    print(output)
    return output


def write_file(filename, output):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for out in output:
            f.write(out + '\n')

def main():
    chat = read_file('input.txt')
    output = convert(chat)
    write_file('output.txt', output)

main()