from blocks import Blocks, block_dataset

blocks = Blocks(block_dataset) 

# print("test", block.block_list)
print("test", blocks.block_used)
print("mark #2 block used")
blocks.show_blocks()
blocks.mark_used(2)
blocks.show_blocks()