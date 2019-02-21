chat = []
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        chat.append(line.strip())
print(chat)