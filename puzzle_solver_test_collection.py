import collections

Block = collections.namedtuple('Block', ['dim', 'shape'])
Block2 = collections.namedtuple('Block2', ['shape', 'size'] )
Block3 = collections.namedtuple('Block3', ['shape', 'size', 'shape_fill', 'id'] )
# block = Block((2,2), [(1,1),(2,2)])
# block2 = [Block2('o'), Block2('xox;xox;ooo')]

class Puzzle:
    shapes = ['o',
        'xox;xox;ooo',
        'xox;ooo;xox',
        'oxx;oox;xoo',
        'oo;ox;ox',
        'ooxx;xooo',
        'oooo;xoxx',
        'xxo;ooo',
        'xox;ooo;xxo',
        'o;o;o;o;o',
        'oo;xo;xo']
    
    def __init__(self):
        # self.dims = [ (len(shape.split(';')),len(shape.split(';')[0])) for shape in self.shapes ]
        # self._blocks = [Block2(shape, (len(shape.split(';')),len(shape.split(';')[0])) ) for shape in self.shapes]
        self._blocks = []
        for shape in self.shapes:
            shape_list = shape.split(';')
            shape_fill = []
            for i,r in enumerate(shape_list):
                for j,c in enumerate(r):
                    if c=='o':
                        shape_fill.append((i,j))

            self._blocks.append( Block3(shape, (len(shape_list),len(shape_list[0])), shape_fill, len(self._blocks)) )


    def __len__(self):
        return len(self._blocks)
    def __getitem__(self, position):
        return self._blocks[position]
    
    
puzzle = Puzzle()
# print(puzzle._blocks)
# for b in puzzle._blocks:
#     print(b)

table_row = 6
table_column = 8
table = {}
for r in range(table_row):
    for c in range(table_column):
        table[r,c]=False

def load_block(coor, block : Block3):
    # move coordination
    fill_list = []
    for e in block.shape_fill:
        fill_list.append((e[0]+coor[0], e[1]+coor[1]))
    # check if loadable
    for f in fill_list:
        if table[f] == True:
            return False
    # fill table and return
    for f in fill_list:   
        table[f]=True
    return True
        


def loop_block( block_list : list):
    for B in block_list:
        load_complete = False
        for k,v in table.items():
            if v == False:
                if load_block((r,c),B) == False:
                    next
                else:
                    load_complete = True
                    break
        if load_complete == False:
            return False
        else:
            next
    return True

print(loop_block(puzzle._blocks))

                