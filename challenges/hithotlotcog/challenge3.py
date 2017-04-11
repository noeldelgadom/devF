import itertools

def areAdjacent(word1, word2):
    count = 1                                   # Initialize at 1 given words can deviate by 1 letter
    list1, list2 = list(word1), list(word2)     # Make lists out of the words
    zipped = zip(list1, list2)                  
    for pair in zipped:                         # A pair is (0,0) where 0 denotes the position on the word
        if pair[0] is pair[1]:                  # Check if the letters at the positions are the same
            count += 1
    return True if count is len(word1) else False

# Inputs
beginWord = 'hit'
endWord = 'cog'
wordList = ['hot','dot','dog','lot','log','cog']

# Get all posstible combinations of the wordList
combinations = list(itertools.permutations(wordList, len(wordList)))
feasible = []

for combination in combinations:
    combination = list(combination)             # Convert individual tuple to list
    combination.insert(0, beginWord)            # Insert beginWord at beginning
    for position in range(len(wordList)):       # Check all positions in combination
        word1 = combination[position]
        word2 = combination[position+1]
        if not areAdjacent(word1, word2):
            break
        if word2 is endWord:                    # Determine if the endWord has been found
            feasible.append(combination[:position+2])
            break

if feasible:
    output = []
    shortest = len(wordList)
    print('The feasible paths are: ')
    print('---')
    for path in feasible:
        if ', '.join(path) not in output:           # Eliminate repeated paths
            output.append(', '.join(path))
            shortest = min(shortest, len(path))     # Determine shortest path
    for path in output:                             # Print them out nicely
        print(path)
    print('---')
    print('The shortest of which is %s words long' % shortest)
else:
    print('--- Ooops! There are no feasible paths ---')