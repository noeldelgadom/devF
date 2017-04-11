import itertools

beginWord = 'hit'
endWord = 'cog'
wordList = ['hot','dot','dog','lot','log','cog']
test = ['a','b','c']

combinations = list(itertools.permutations(test, len(test)))
print(combinations)
