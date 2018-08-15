def getMostFrequentWords(wordsToExclude, literatureText):
    if len(literatureText) == 0:
        return []
    wordsToExclude = set(wordsToExclude)
    wordMap = {}
    for word in literatureText.split(' '):
        if word not in wordsToExclude:
            if word not in wordMap:
                wordMap[word] = 1
            else:
                wordMap[word] += 1

    wordCountPairs = [(word, wordMap[word]) for word in wordMap]
    sortedWordCountPairs = sorted(wordCountPairs, key=lambda a: a[1], reverse=True)
    mostFreqWords = []
    maxCount = sortedWordCountPairs[0][1]
    for word, count in sortedWordCountPairs:
        if count == maxCount:
            mostFreqWords.append(word)
        else:
            break

    return mostFreqWords

wordsToExclude = ['to', 'or', 'a']
literatureText = 'Soren went to a class or concert came back with a guitar guitar guitar'
print(getMostFrequentWords(wordsToExclude, literatureText))