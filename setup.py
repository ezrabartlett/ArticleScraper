import scraper
import json
import reccommendations

def main():
    # Start the scraper. The scraper combs designated sites for articles and performs some clustering algorithms on them.
    data = scraper.processData()
    
    #for cluster in data['clusters']:
    #    for document in cluster['points']:
    #        print(document['title'])
    #    print("============================")
    
    # Save the data to a text file, to be displayed by the frontend
    #with open('ArticleData.txt', 'w') as outfile:
    #    json.dump(data, outfile)

    #with open('ArticleData.txt') as json_file:
    #    data = json.load(json_file)
    
    for cluster in data['clusters']:
        for article in cluster['points']:
            reccs = []
            reccs = reccommendations.getReccomendations(article, cluster['points'])
            
            related = []
            for rec in reccs:
                related.append({'id': str(rec[1]['id']), 'title': rec[1]['title']})
            
            article.update({'related': related})
    
    # Create a tree structure that's easier for javascript to read
    articles = {}
    for cluster in data['clusters']:
        for document in cluster['points']:
            docPod = {
                'title': document['title'],
                'content': document['content'],
                'related': document['related']
            }
            if str(document['id']) not in articles:
                articles.update({str(document['id']): docPod})

    #Save the data to a text file, to be displayed by the frontend
    with open('./FrontendFiles/bakedData.json', 'w') as outfile:
        json.dump(articles, outfile)
    
main()
