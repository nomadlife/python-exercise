filename = 'lee'
with open (filename) as file:
    data = file.read().split('\n')
print(len(data))
# print(data[:10])

for w in data:
    if w != '' :
        target = w.rindex('.')
        if target < 5  :
            # target_2 = w[:target].rindex(' ')+1
            print(w)
