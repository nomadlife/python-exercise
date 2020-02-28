import itertools

# sample = list(itertools.permutations([1, 2, 3,4,5,6,7,8,9,10,11]))
# print(len(sample))

sample = list(itertools.permutations(range(11)))
print(len(sample))
print(sample[:10])