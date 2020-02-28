from blocks import Blocks, block_dataset
from puzzle import Puzzle

# blocks = Blocks(block_dataset) 
puzzle = Puzzle(6,8,block_dataset)

position = 0
if position == 0 and puzzle.blocks.block_list[0].offset == 2:
        pass
else:
    for ti,tv in puzzle.table.items():
        if tv == "x" :
            if puzzle.isLoadable(ti, puzzle.blocks.block_list[position]):
                puzzle.load_block(ti,puzzle.blocks.block_list[position])
                position += 1
                print(ti,puzzle.blocks.block_list[position].id, end='block loaded; ')
            else:
                pass
                # print(ti,b.id, end='; ')
print()
puzzle.show_table()
puzzle.isFull()
puzzle.blocks.show_blocks()