def read_file(filename):
    chat = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())
    return chat

def convert(chat):
    person = None
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    vike_word_count = 0
    vike_sticker_count = 0
    vike_image_count = 0
    for line in chat:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            if s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                    vike_sticker_count += 1
            if s[2] == '圖片':
                    vike_image_count += 1
            else:
                for m in s[2:]:
                    vike_word_count += len(m)
    print('allen說了', allen_word_count, '個字')
    print('allen傳了', allen_sticker_count, '個貼圖')
    print('allen傳了', allen_image_count, '張圖片')
    print('vike說了', vike_word_count, '個字')
    print('vike傳了', vike_sticker_count, '個貼圖')
    print('viki傳了', vike_image_count, '張圖片')
        # print(s)


def write_file(filename, output):
    with open(filename, 'w', encoding = 'utf-8-sig') as f:
        for out in output:
            f.write(out + '\n')

def main():
    chat = read_file('-LINE-Viki.txt')
    output = convert(chat)
    # write_file('output.txt', output)

main()