import sys

if len(sys.argv) > 1:
    # print(sys.argv[1])
    filename = sys.argv[1]
    with open (filename,'r') as file:
        data = [line.rstrip().split(' ') for line in file.readlines()]
    # print(len(data))
    # print(data[0])

    result = {}
    for d in data:
        char = d[0][0].upper()
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    for k,v in result.items():
        print(k,k*v, v)