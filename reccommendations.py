import helpers

# I expected more to be in here. This file and its sole function look at a given article and cluster and make what is essential a similariy map, where there is a one way connection between the article in question and the 5 closest articles in the given set.

# Basically the KNN algorithm, but works suprisingly well when data has already been seperated into clusters by K-mean
def getReccomendations(data, set):
    
    K = 5
    article = data['frequencyVector']
    K_closest = []
    
    for document in set:
        similarity = helpers.cosineSimilarity(document['frequencyVector'], article)
        index = 0
        flag = 0
        for i,item in enumerate(K_closest):
            if similarity>item[0]:
                index = i
                flag = 1
                break
        if(document['title']==data['title']):
            continue
        if(flag):
            K_closest.insert(index, [similarity, document])
        else:
            K_closest.append([similarity, document])
        
        if(len(K_closest)>K):
            K_closest = K_closest[:K]
            
    return K_closest
