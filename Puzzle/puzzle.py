# Puzzle Class
from block import Block
from blocks import Blocks

class Puzzle:
    
    def __init__(self, row, column, block_input, init_list=None):
        if row == None or column == None or block_input == None:
            print('argument : row, col, block_list, init_list.')
        else:
            # self.dimension = (row, column)
            self.blocks = Blocks(block_input)
            self.table_row = row
            self.table_col = column
            length = row * column
            self.table = {n:'x' for n in range(1,length + 1)}
            if init_list == None:
                self.init_list = []
            else :
                self.init_list = init_list
                print("init_list :", self.init_list)
                self.load_block_init()


            print('table created. row:',row,' x col:',column)

    def load_block_init(self):
        print('fn called')
        for n,b in self.init_list:
            if self.isLoadable(n,self.blocks.block_list[b]):
                self.load_block(n,self.blocks.block_list[b])
            else:
                print("load not possible. place :", n, b," th block")

    def table_init(self):
        self.table = {n:'x' for n in range(1,len(self.table) + 1)}
        return self
    
    def show_list(self):
        result = ''
        for _,v in self.table.items():
            result+=str(v)
        print(result)
        return self

    def show_table(self):
        result = ''
        for k,v in self.table.items():
            if v == 'x':
                result += '.x'
            else:
                result += v.zfill(2)

            if k%self.table_col == 0:
                result += '\n'
        print(result)
        return self

    def isLoadable(self, n, block, offset_trigger=False):
        loadable = True

        offset = 0
        if offset_trigger == True and n != 1:
            offset = block.offset

        if (n-1)%8 + block.col > 8:
            loadable = False
        elif (n-1)//8 + block.row > 6:
            loadable = False
        else:
            for e in block.data:
                if self.table[e+n-1-offset] == 'x':
                    pass
                else:
                    loadable = False
                    break
        # print(loadable, block.offset)
        return loadable

    def isLoadableAny(self, block : Block):
        loadable = False
        for i,v in self.table.items():
            if self.isLoadable(i,block):
                loadable = i
                break
        return loadable
    
    def load_block(self, n : int, block : Block, offset_trigger=False):
        
        offset = 0
        if offset_trigger == True and n != 1:
            offset = block.offset

        # print("load_block() called", n, block.id)
        for e in block.data:
            self.table[e+n-1-offset] = str(block.id)
        # print("block loaded")
        self.blocks.mark_used(block.id)
        return self
    
    # def load_block_front(self, block : Block):
    #     check = self.isLoadableAny(block)
    #     if check != False:
    #         self.load_block(check, block)
    #         return self
    #     else:
    #         print("no space for block ", block.id)
    #         return None
    
    def isFull(self):
        result = True
        for _,v in self.table.items():
            if v=="x":
                result = False
        # print(result)
        return result