# hold

from blocks import Blocks, block_dataset
from puzzle import Puzzle

# blocks = Blocks(block_dataset) 
puzzle = Puzzle(6,8,block_dataset)

# for b in puzzle.blocks.block_list:
#     check = puzzle.isLoadableAny(b)
#     if check != False:
#         puzzle.load_block(check, b)

for block in puzzle.blocks.block_list:
    result = puzzle.isLoadableAny(block)
    if result != False:
        puzzle.load_block(result, block)
        # blocks.mark_used(block.id)
    else:
        print("***no space for block ",block.id)

puzzle.show_table()
puzzle.blocks.show_blocks()
print(puzzle.isFull())
