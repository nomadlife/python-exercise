from puzzle import Puzzle
from blocks import block_dataset

'''
01.x.x.x.x.x.x.x
01.x.x.x.x.x.x.x
01.x.x.x.x.x.x.x
01.x.x.x.x.x.x.x
01.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x (1,3~6,8) (1,2)

.x02.x.x.x.x.x.x
.x02.x.x.x.x.x.x
020202.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x (2~5)(1) (1-6)(2-4)
(25~30,2)

.x03.x.x.x.x.x.x
030303.x.x.x.x.x
.x03.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x


04.x.x.x.x.x.x.x
0404.x.x.x.x.x.x
.x0404.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x ()

0505.x.x.x.x.x.x
05.x.x.x.x.x.x.x
05.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x

0606.x.x.x.x.x.x
.x060606.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x

07070707.x.x.x.x
.x07.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x  (1~5)

.x.x08.x.x.x.x.x
080808.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x  (38,8)

.x09.x.x.x.x.x.x
090909.x.x.x.x.x
.x.x09.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x

1010.x.x.x.x.x.x
.x10.x.x.x.x.x.x
.x10.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x

11.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x
.x.x.x.x.x.x.x.x

'''
puzzle = Puzzle(6,8,block_dataset)
# puzzle = Puzzle(6,8,block_dataset)

# print("test", block.block_list)
puzzle.show_list()
puzzle.show_table()
puzzle.load_block(1,puzzle.blocks.block_list[6])
puzzle.show_table()
if puzzle.isLoadable(5,puzzle.blocks.block_list[7]):
    puzzle.load_block(5,puzzle.blocks.block_list[7])
puzzle.show_table()