chat = []
with open('input.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        chat.append(line.strip())
print(chat)

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

with open('output.txt', 'w', encoding = 'utf-8') as f:
    for out in output:
        f.write(out + '\n')