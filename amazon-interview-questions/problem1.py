def retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude):
    # WRITE YOUR CODE HERE
    words = breakIntoWords(literatureText)
    wordsToExclude = set(wordsToExclude)
    freqMap = {}
    for word in words:
        if word not in wordsToExclude:
            if word not in freqMap:
                freqMap[word] = 1
            else:
                freqMap[word] += 1
    sortedMap = sortMap(freqMap)
    return sortMap[0][0]


def breakIntoWords(sentence):
    sentence = sentence.lower()
    words = sentence.split(' ')
    return words


def sortMap(m):
    t = [(key, m[key] for key in m]
    return sorted(t, key=lambda item: item[1])