import bs4
import requests
import kmeans
import helpers
import json

r1 = requests.get('https://www.cnn.com/entertainment')

# Grab all of the links for a specific section of CNN's website
def grabCnnLinks(url):
    response = requests.get(url).content
    soup = bs4.BeautifulSoup(response, 'html.parser')
    links = soup.findAll('a')
    
    articleLinks = []
    
    for article in links:
        link = article.get('href')
        if(link[:8]=='/2020/03' or link[:8]=='/2020/04'):
            articleLinks.append(link)
    
    return articleLinks

# CNN specific parser. Gets title and body of an articles
def parseCnnArticle(url):
    article = {}
    
    response = requests.get(url).content
    soup = bs4.BeautifulSoup(response, 'html.parser')
    title = soup.h1#findAll('h1', class_='pg-headline', limit=1)
    body = soup.findAll(class_='zn-body__paragraph')
    
    content = ""
    
    for paragraph in body:
        content += paragraph.get_text()+" <br><br>"
        
    article.update({'title': title.get_text(),'content': content[6:]})
    
    return article
    #print(article)
    
    #print("=======================================================")

# Get a list of all articles on the top CNN web pages
def getCNNArticles():
    
    entertainment = grabCnnLinks('https://www.cnn.com/entertainment')
    scienceLinks = grabCnnLinks('https://www.cnn.com/specials/space-science')
    world = grabCnnLinks('https://www.cnn.com/world')
    US = grabCnnLinks('https://www.cnn.com/us')
    tech = grabCnnLinks('https://www.cnn.com/business/tech')
    politics = grabCnnLinks('https://www.cnn.com/politics')
    
    allLinks = entertainment+scienceLinks+world+US+tech+politics
    allLinks = list(dict.fromkeys(allLinks))
    articles = []
    
    for i,link in enumerate(allLinks):
        print(str(i)+" of "+str(len(allLinks))+" documents parsed")
        article = parseCnnArticle('https://www.cnn.com'+link)
        if(len(article['content'])>5):
            articles.append(article)
        
    return articles

# Run each news site's respective function
def getArticles():
    articles = []
    
    articles += getCNNArticles()
    
    for i,article in enumerate(articles):
        article.update({'id':i})
        freq = helpers.parseDocument(article)
        norm = helpers.EuclidNorm(freq)
        article.update({'frequencyVector':freq, 'normalizedVector':norm})
    
    return articles

def processData():
    articles = getArticles()
    
    articlesDict = {
        'articles': articles
    }
    
    with open('Articles.txt', 'w') as outfile:
           json.dump(articlesDict, outfile)
    
    clusters = kmeans.cluster(5, articles)
    
    data = {
        'clusters': clusters
    }
    
    return data
