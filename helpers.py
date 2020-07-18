import math

def parseDocument(document):
    wordBag = document['content'].split()
    frequencyVector = {}
    for word in wordBag:
        if(word.lower() in frequencyVector):
            frequencyVector[word.lower()]=frequencyVector[word.lower()]+1
        else:
            frequencyVector.update( {word.lower() : 1} )
    return frequencyVector

def cosineSimilarity(docA, docB):
    # Get list of all words in both documents
    allKeys = list(docA.keys())+list(docB.keys())
    # Remove duplicates
    allKeys = list(dict.fromkeys(allKeys))

    AiBi = 0
    Ai_2 = 0
    Bi_2 = 0

    for term in allKeys:
        Ai = 0
        Bi = 0

        if(term in docA):
            Ai = docA[term]
        if(term in docB):
            Bi = docB[term]

        AiBi += Ai*Bi
        Ai_2 += Ai*Ai
        Bi_2 += Bi*Bi
    
    if(Ai_2==0 or Bi_2==0):
        return 10000000
    
    similarity = AiBi/((math.sqrt(Ai_2)*math.sqrt(Bi_2)))
    return similarity
    
# Get the Euclidean norm of a frequency vector
def EuclidNorm(freqVector):
    sum_2 = 0

    for word in freqVector:
        sum_2 += freqVector[word]**2
    
    norm = math.sqrt(sum_2)

    normalizedVector = {}

    for word in freqVector:
        normalizedVector.update( { word : freqVector[word]/norm } )

    return(normalizedVector)

# Gets the euclidean distance between two vectors
def euclideanDistance(docA, docB):
    # Get list of all words in both documents
    allKeys = list(docA.keys())+list(docB.keys())
    # Remove duplicates
    allKeys = list(dict.fromkeys(allKeys))

    diffSum = 0

    for term in allKeys:
        Ai = 0
        Bi = 0

        if(term in docA):
            Ai = docA[term]
        if(term in docB):
            Bi = docB[term]

        diff = (Ai - Bi)**2
        
        diffSum+=diff

    distance = math.sqrt(diffSum)
    return distance


# Calculate the centroid of a list of vectors
def calculateCentroid(documents):
    vectorSum = {}

    # Sum all vectors in the list
    for document in documents:
        vector = document['normalizedVector']
        for word in vector:
            if word in vectorSum:
                vectorSum[word] += vector[word]
            else:
                vectorSum.update({word : vector[word]})

    for word in vectorSum:
        vectorSum[word] = vectorSum[word]/len(documents)

    return vectorSum

# Get the Euclidean norm of a frequency vector
def EuclidNorm(freqVector):
    sum_2 = 0

    for word in freqVector:
        sum_2 += freqVector[word]**2
    
    norm = math.sqrt(sum_2)

    normalizedVector = {}

    for word in freqVector:
        normalizedVector.update( { word : freqVector[word]/norm } )

    return(normalizedVector)
