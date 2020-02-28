# test for display

from blocks import Blocks, block_dataset
from puzzle import Puzzle
import itertools

puzzle = Puzzle(6,8,block_dataset)

loops = list(itertools.permutations(range(11)))[:40000]

for i,loop in enumerate(loops):
    # print(loop)
    position = 0
    if puzzle.blocks.block_list[loop[0]].offset == 2:
        continue
        
    for n in range(1,49):
        if n == 1:
            puzzle.load_block(n, puzzle.blocks.block_list[loop[position]])
            position += 1
        elif puzzle.table[n] == "x" :
            if puzzle.isLoadable(n, puzzle.blocks.block_list[loop[position]], offset_trigger=True):
                puzzle.load_block(n, puzzle.blocks.block_list[loop[position]], offset_trigger=True)
                position += 1
                # print(ti,puzzle.blocks.block_list[position].id, end='block loaded; ')

        
        # else:
        #     print("***no space for block ",block.id)
    # puzzle.show_table()
    # puzzle.blocks.show_blocks()
    # print(puzzle.isFull())
    
    if puzzle.isFull():
        puzzle.show_table()
        print("table",i,loop)
    puzzle.table_init()
    # puzzle.blocks.mark_init()


#     if puzzle.isFull():
#         finished = True
#         break
# if finished = True:
#     break

