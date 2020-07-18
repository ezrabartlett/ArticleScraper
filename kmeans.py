import random
import helpers

data = []
kpoints = []
clusters = []
k = 0

def createClusters(iterations):
    for i in range(iterations):
        global data
        
        # Reset clusters
        for cluster in clusters:
            cluster['points'] = []
        
        # Loop over all documents and assign each document to the nearest cluster
        for point in data:
            nearest = 9999
            nearestIndex = 0
            
            for i,cluster in enumerate(clusters):
                distance = helpers.euclideanDistance(point['frequencyVector'], cluster['centroid'])
                
                if(distance<nearest):
                    nearest = distance
                    nearestIndex = i
                    
            clusters[nearestIndex]['points'].append(point)
        
        # Recalculate centroids
        for cluster in clusters:
            centroid = helpers.calculateCentroid(cluster['points'])

def getKPoints(k):
    global data
    global clusters
    
    for i in range(k):
        choice = random.choice(data)
        while choice in kpoints:
            choice = random.choice(data)
            
        clusters.append({'centroid': choice['frequencyVector'], 'points':[]})

def cluster(n, dataPoints):
    global data
    global clusters
    global k
    k = n
    data = dataPoints
    getKPoints(k)
    createClusters(20)
    
    return clusters
