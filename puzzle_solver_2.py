# shapes = ['o',
#         'xox;xox;ooo',
#         'xox;ooo;xox',
#         'oxx;oox;xoo',
#         'oo;ox;ox',
#         'ooxx;xooo',
#         'oooo;xoxx',
#         'xxo;ooo',
#         'xox;ooo;xxo',
#         'o;o;o;o;o',
#         'oo;xo;xo']
import collections
Block = collections.namedtuple('Block', ['shape', 'size', 'shape_fill', 'id'] )

blocks = [(0),
            (0,8,15,16,17),
            (0,7,8,9,16),
            (0,8,9,16,17),
            (0,1,8,16),
            (0,1,8,16),
            (0,1,9,10,11),
            (0,1,2,3,9),
            (0,6,7,8),
            (0,7,8,9,17),
            (0,8,16,24,32),
            (0,1,9,17)
            ]


class Puzzle:
    table_row = 6
    table_column = 8
    table = {}
    
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
        self.new()
        
        self._blocks = []
        for shape in self.shapes:
            shape_list = shape.split(';')
            shape_fill = []
            for i,r in enumerate(shape_list):
                for j,c in enumerate(r):
                    if c=='o':
                        shape_fill.append((i,j))

            self._blocks.append( Block(shape, (len(shape_list),len(shape_list[0])), shape_fill, len(self._blocks)) )


    def __len__(self):
        return len(self._blocks)
    
    def __getitem__(self, position):
        return self._blocks[position]
    
    def new(self):
        for r in range(self.table_row):
            for c in range(self.table_column):
                self.table[r,c]=False
        return self
        
    def show_table(self):
        #print('table size : {} x {}'.format(table_row, table_column))
        result = ''
        for r in range(self.table_row):
            for c in range(self.table_column):
                if self.table[(r,c)] == False:
                    result+='x'
                else:
                    result+=self.table[(r,c)]
            result+='\n'
        print(result)
        
    def load_block(self, coor, block : Block):
        # move coordination
        fill_list = []
        for e in block.shape_fill:
            new_row = e[0]+coor[0]
            new_collumn = e[1]+coor[1]
            
            fill_list.append((new_row, new_collumn))
        # check if loadable
        for f in fill_list:
            if f in self.table and self.table[f] == True:
                return False
        # fill table and return
        for f in fill_list:   
            self.table[f]=str(block.id)
            
#         self.show_table()
        return self
        
print(blocks[1])