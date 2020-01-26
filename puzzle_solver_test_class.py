import collections

Block = collections.namedtuple('Block', ['dimension', 'shape'])

class Puzzle:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    # dim_list = []
    # shape_list = []

    def __init__(self):
        self._blocks = [Block(rank, suit) for suit in self.suits for rank in self.ranks]
    def __len__(self):
        return len(self._blocks)
    def __getitem__(self, position):
        return self._blocks[position]
    def get_ranks(self):
        return self.ranks

puzzle = Puzzle()
print(len(puzzle))
print(puzzle.get_ranks())
