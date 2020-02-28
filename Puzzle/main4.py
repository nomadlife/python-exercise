# full test
# almost done,, hold
import time
from blocks import Blocks, block_dataset
from puzzle import Puzzle
import itertools

start = time.time()
puzzle = Puzzle(6,8,block_dataset)
loops = list(itertools.permutations(range(11)))

for n,loop in enumerate(loops):
    # print(loop)
    position = 0
    if puzzle.blocks.block_list[loop[0]].offset == 2:
        continue
        
    for n in range(1,49):
        block = puzzle.blocks.block_list[loop[position]]
        if n == 1:
            puzzle.load_block(n, block)
            position += 1
        elif puzzle.table[n] == "x" :
            if puzzle.isLoadable(n, block, offset_trigger=True):
                puzzle.load_block(n, block, offset_trigger=True)
                position += 1
        
        # else:
        #     print("***no space for block ",block.id)
    # puzzle.show_table()
    # blocks.show_blocks()
    if puzzle.isFull():
        print(n,loop)
        puzzle.show_table()
        break
    else :
        puzzle.table_init()
    # puzzle.blocks.mark_init()
    
    # print("loop: %d"%n, end='\r', flush=True)
    # sys.stdout.write("loop: %d"%(i) )
    # sys.stdout.flush()

#     if puzzle.isFull():
#         finished = True
#         break
# if finished = True:
#     break

print("calc time :", time.time() - start)