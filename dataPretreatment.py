
from config import *
import numpy as np

def pretreatment(filename):
    poems = []
    file = open(filename, "r")
    for line in file: 
        try:
            title, poem = line.strip().split(":") 
        except:
            continue
        poem = poem.replace(' ','')
        if '_' in poem or '《' in poem or '[' in poem or '(' in poem or '（' in poem:
            continue
        if len(poem) < 10 or len(poem) > 128: 
            continue
        poem = '[' + poem + ']' 
        poems.append(poem)

    print("唐诗总数： %d"%len(poems))
    allWords = {}
    for poem in poems:
        for word in poem:
            if word not in allWords:
                allWords[word] = 1
            else:
                allWords[word] += 1
    wordPairs = sorted(allWords.items(), key = lambda x: -x[1])
    words, a= zip(*wordPairs)
    words += (" ", )
    wordToID = dict(zip(words, range(len(words)))) 
    wordTOIDFun = lambda A: wordToID.get(A, len(words))
    poemsVector = [([wordTOIDFun(word) for word in poem]) for poem in poems] # poem to vector
    batchNum = (len(poemsVector) - 1) // batchSize
    X = []
    Y = []
    for i in range(batchNum):
        batch = poemsVector[i * batchSize: (i + 1) * batchSize]
        maxLength = max([len(vector) for vector in batch])
        temp = np.full((batchSize, maxLength), wordTOIDFun(" "), np.int32)
        for j in range(batchSize):
            temp[j, :len(batch[j])] = batch[j]
        X.append(temp)
        temp2 = np.copy(temp) 
        temp2[:, :-1] = temp[:, 1:]
        Y.append(temp2)

    return X, Y, len(words) + 1, wordToID, words


