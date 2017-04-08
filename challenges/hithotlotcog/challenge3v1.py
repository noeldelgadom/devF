def determineOptions(beginWord,endWord,wordList):    # Función que genera opciones posibles
    alphabet = [chr(one) for one in range(97,123)]
    options = []
    for i in range(len(beginWord)):
        for j in range(len(alphabet)):
            options.append(beginWord[0:i] + alphabet[j] + beginWord[(i+1):len(beginWord)])
            #La lista options tienes todas las posibles opciones al cambiar una letra en beginWord
    feasibleOptions = [word for word in wordList if word in options]
            #feasibleOptions filtra todas las opciones y deja las que existen en la lista original de wordList
    if len(feasibleOptions) != 0:
        return feasibleOptions
    else:
        return False
        
def findLinks(beginWord, endWord, wordList):
    count = 0
    if determineOptions(beginWord, endWord, wordList) == False:         # Determine if a variation of beginWord is in wordList
        return count                                                        # Return 0 when the variation is absent from wordList
    else:
        count += 1
        newPaths = determineOptions(beginWord, endWord, wordList)       # Determine possible new paths
        wordList = [word for word in wordList if word not in newPaths]  # Eliminate used words from wordList
        global paths
        for newWord in newPaths:                                        # Appends the new word to the list paths
            paths.append(beginWord + newWord)
            findLinks(newWord, endWord, wordList)
    links = paths[1:len(paths)]
    return links
    
def wordLadder(beginWord, endWord, wordList):
    links = findLinks(beginWord, endWord, wordList)
    feasiblePaths = links[0]
    for first in links:
        print(first)
    return feasiblePaths
    
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
paths = [beginWord]
    
print([beginWord] + [beginWord] + [beginWord])
print((beginWord + endWord)[:len(endWord)])
print((beginWord + endWord)[len(endWord):])
print(wordLadder(beginWord, endWord, wordList))