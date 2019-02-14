filename = 'ws1'
with open (filename) as file:
    data = file.readlines()
print(len(data))
print(data[:10])
for w in data[:100]:
    if len(w) < 10:
        print(w)
    else:
        print(w[:10])