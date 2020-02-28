table={i:'x' for i in range(48)}
# print(table)

blocklist = [(1,),
(2, 10, 17, 18, 19),
(2, 9, 10, 11, 18),
(1, 9, 10, 18, 19),
(1, 2, 9, 17),
(1, 2, 10, 11, 12),
(1, 2, 3, 4, 10),
(3, 9, 10, 11),
(2, 9, 10, 11, 19),
(1, 9, 17, 25, 33),
(1, 2, 10, 18)]

# print(blocklist)

def show_table():
    result = ''
    for k,v in table.items():
        if v == 'x':
            result += '.x'
        else:
            result += v.zfill(2)

        if (k+1)%8 == 0:
            result += '\n'

    print(result)

# show_table()

def table_init():
    for k,v in table.items():
        table[k] == 'x'

