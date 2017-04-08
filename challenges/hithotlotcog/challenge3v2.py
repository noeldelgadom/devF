import copy

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
children = [determineOptions(word, endWord, wordList) for word in wordList] # lista que tontiene los posibles hijos de cada uno. 
for i in range(len(wordList)):
    children[i].remove(wordList[i])                                         # Quitarle a si mismo


path = [[beginWord]]
pathCount = 0
availableWords = [wordList[:]]

current = beginWord
newPaths = determineOptions(current,endWord,wordList)
pathCount += len(newPaths)
print("Path", path)
print("Current Word:", current)
print("Available Words", availableWords)
print("New Path", newPaths)
print("---")

for i, word in enumerate(newPaths):
    path.append(path[len(path)-i-1] + [word])
    availableWords.append([j for j in wordList if not j in path[-1]])
    print("Path", path)
    print("Current Word:", current)
    print("Working Word:", word)
    print("Available Words", availableWords)
    print("New Path", newPaths)
    print("---")