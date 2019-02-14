filename = 'ws1'
with open (filename) as file:
    data = [line.split('\t') for line in file.read().split('\n')]
# print(len(data))
# print(data[10][1])
# for w in data[900:]:
#     if len(w) < 10:
#         print(w)
#     else:
#         print(w[:10])

unicode_kor = ord('가')

f = open('output_kor.txt','w')

for j in range(len(data)):
    # print(data[j])

    # if len(data[j]) != 2:
    #     print(len(data[j]), data[j])
    if data[j] == ['']: break
    else : string = data[j][1]

    for i in range(len(string)):
        if ord(string[i]) >= unicode_kor and ord(string[i-1]) == 32:
            # print(i, string[i], ord(string[i]))\
            # print(j, string[:i])
            # print(data[j][0], string[i:])
            print(string[i:])
            f.write(string[i:] + '\n')
            break

f.close