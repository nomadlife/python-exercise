# Block class
from block import Block
'''
'o','xox;xox;ooo',
'xox;ooo;xox',
'oxx;oox;xoo',
'oo;ox;ox',
'ooxx;xooo',
'oooo;xoxx',
'xxo;ooo',
'xox;ooo;xxo',
'o;o;o;o;o',
'oo;xo;xo'
'''
block_dataset = [
            'o;o;o;o;o',
            'xox;xox;ooo',
            'xox;ooo;xox',
            'oxx;oox;xoo',
            'oo;ox;ox',
            'ooxx;xooo',
            'oooo;xoxx',
            'xxo;ooo',
            'xox;ooo;xxo',
            'oo;xo;xo','o']
    
class Blocks:

    def __init__(self, block_input):
        self.block_numbers = len(block_input)
        self.block_used = {n+1:False for n in range(self.block_numbers)}
        self.block_list = []
        for i,shape in enumerate(block_input):
            row = shape.count(';')+1
            col = len(shape.split(';')[0])
            data = self.shape2data(shape)
            fill = len(data)
            offset = data[0]-1 if data[0]>1 else 0
            self.block_list.append(Block(i+1, shape, data, offset, fill, row, col,  False))
            
        print("block data created : ",len(self.block_list))

    def show_blocks(self):
        for b in self.block_list:
            if self.block_used[b.id] == True:
                print("{:2} Used".format(b.id))
            else:
                print("{:2}     Unused".format(b.id))

    def mark_used(self, n):
        self.block_used[n] = True

    def mark_init(self):
        for k,v in self.block_used.items():
            self.block_used[k] = False 
        
    def convert_serial(self, shapes: list) -> list:
        block_data = []
        for shape in shapes:
            shape_number = []
            position = 1
            for s in shape:
                if s == 'o':
                    shape_number.append(position)
                    position += 1
                elif s == 'x':
                    position += 1
                elif s == ';':
                    if position <= 8: position = 9
                    elif position <= 16: position = 17
                    elif position <= 24: position = 25
                    elif position <= 32: position = 33
                    elif position <= 40: position = 41
            block_data.append(tuple(shape_number))
        return block_data
    
    def shape2data(self, shape):
        shape_number = []
        position = 1
        for s in shape:
            if s == 'o':
                shape_number.append(position)
                position += 1
            elif s == 'x':
                position += 1
            elif s == ';':
                if position <= 8: position = 9
                elif position <= 16: position = 17
                elif position <= 24: position = 25
                elif position <= 32: position = 33
                elif position <= 40: position = 41
        return tuple(shape_number)