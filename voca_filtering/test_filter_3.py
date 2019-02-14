filename = 'lee_2'
with open (filename) as file:
        data = [line.split('. ') for line in file.read().split('\n')]
print(len(data))
print(data[:10])


for i in data:
        if i != ['']:
                # print(i[0].zfill(3), i[1])
                i[0] = i[0].zfill(4)
                # print(i)

data.sort()

f1 = open('lee_3_word', 'w')
f2 = open('lee_3_meaning', 'w')
for d in data:
        try :
                string = d[1]
                cut = 0
                for i,v in enumerate(string):
                        if v == '∼' and string[i-1] == ' ':
                                cut = i
                                break
                        elif v == '~' and string[i-1] == ' ':
                                cut = i
                                break
                        elif v == '(' and string[i-1] == ' ' : 
                                cut = i
                                break
                        elif ord(v) >= ord('가') and string[i-1] == ' ':
                                cut = i
                                break
                        elif v in 'abcdefghijklmnopqrstuvwxyz' and ord(string[i+1]) >= ord('가'):
                                cut = i + 1
                                break
                if '(' in string:
                        end = string.rindex('(')
                        print('{:4} {:20} {:30} {:40}'.format(d[0], string[:cut], string[cut:end], string[end:]))
                        f1.write(string[:cut]+'\n')
                        f2.write(string[cut:end]+'\n')
                else:
                        print('{:4} {:20} {:30}'.format(d[0], string[:cut], string[cut:]))
                        f1.write(string[:cut]+'\n')
                        f2.write(string[cut:]+'\n')
        except:
                print(d[0], 'error')
f1.close
f2.close

print('~'=='∼')
print(ord('~'), ord('∼'))