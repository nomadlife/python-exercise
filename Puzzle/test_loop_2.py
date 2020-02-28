from blocks import Blocks, block_dataset
from puzzle import Puzzle

# blocks = Blocks(block_dataset)
puzzle = Puzzle(6,8,block_dataset)

puzzle.table_init()
block = puzzle.blocks.block_list[1]
for i,v in puzzle.table.items():
    if puzzle.isLoadable(i, block):
        puzzle.load_block(i, block)
        puzzle.show_table()
        puzzle.table_init()