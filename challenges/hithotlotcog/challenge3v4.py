def determineOptions(beginWord,endWord,wordList):    # Función que genera opciones posibles
    alphabet = [chr(one) for one in range(97,123)]
    options = []
    for i in range(len(beginWord)):
        for j in range(len(alphabet)):
            options.append(beginWord[0:i] + alphabet[j] + beginWord[(i+1):len(beginWord)])
            #La lista options tienes todas las posibles opciones al cambiar una letra en beginWord
    feasibleOptions = [word for word in wordList if word in options]
            #feasibleOptions filtra todas las opciones y deja las que existen en la lista original de wordList
    return feasibleOptions if len(feasibleOptions) != 0 else False
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","hat","dot","dog","lot","log","cog"]

paths = []                  # Where I will place all feasible paths
path = [beginWord]          # An individual path
pathIndex = [0]
nodeOptions = [len(determineOptions(beginWord,endWord,wordList))-1]
availableWords = wordList[:]

print("Paths Content:   ", paths)
print("---")

print("Start Word:      ", beginWord)
print("Path:            ", path)
print("Path Index:      ", pathIndex)
print("Node Options:    ", nodeOptions)
print("Options:         ", determineOptions(beginWord, endWord, availableWords))
print("Available Words: ", availableWords)
print("---")

"""Loop Starts"""

while endWord != path[-1]:
    nextWord = determineOptions(path[-1], endWord, availableWords)[0]#pathIndex[-1]]
    path.append(nextWord)
    if len(pathIndex) is len(nodeOptions):
        pathIndex.append(0)
    availableWords.remove(nextWord)
    if availableWords:
        if determineOptions(path[-1], endWord, availableWords):
            nodeOptions.append(len(determineOptions(path[-1], endWord, availableWords))-1)
        else:
            print(nextWord, "  -->  Wont work")
            path.pop()
            pathIndex[-1] += 1
            nodeOptions[-1] -= 1
    
    print("Next Word:       ", nextWord)
    print("Path:            ", path)
    print("Path Index:      ", pathIndex)
    print("Node Options(-1):", nodeOptions)
    print("Options:         ", determineOptions(nextWord, endWord, availableWords))
    print("Available Words: ", availableWords)
    print("---")

nodeOptions.append(pathIndex[-1])

print("Next Word:       ", nextWord)
print("Path:            ", path)
print("Path Index:      ", pathIndex)
print("Node Options(-1):", nodeOptions)
print("Options:         ", determineOptions(nextWord, endWord, availableWords))
print("Available Words: ", availableWords)
print("---")
paths.append(path)
print("                           Path to Add:                  ", path)
print("                           Feasible Paths:               ", paths)