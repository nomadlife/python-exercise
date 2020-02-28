from blocks import Blocks, block_dataset
from puzzle import Puzzle

# blocks = Blocks(block_dataset)
puzzle = Puzzle(6,8,block_dataset)

puzzle.table_init()
for block in puzzle.blocks.block_list:
    print(block)
    puzzle.load_block(1,block)
    puzzle.show_table()
    puzzle.table_init()