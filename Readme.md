# HOW TO RUN THIS PROJECT

**You must be running Python3 to execute the python scripts. (Made with Python 3.7.0)** 

Install the required packages with pip
```
    pip install -r requirements.txt
```

Run the setup script (if you don't, the site will still work but will use dated articles)
This will take a while to run. Usually about a minute.
```
    python setup.py
```

Change your directory to the FrontendFiles folder. You won't be able to run the program otherwise.
```
    cd FrontendFiles
```

start up a local server using python (you may need to pip install this package if the following command doesnt work. Make sure you're running Python3.7)

```
    python -m http.server 8000
```

you'll see a url pop up in parenthesis
Ex.
http://0.0.0.0:8000/

copy this address and paste it into the search bar of your browser (preferably chrome)

Some random articles from the data set will be displayed, which you can click to read. When you click on an article, related articles will be shown on the side, which you can click on. Click the header bar to return to the main menu.

## Brief description of this project

This project pulls web data from specified sites and uses some classification methods and similarity measuring algorithms to suggest related articles to the user. 

## setup.py

runs the scraper script, which gathers the actual data from the websites. After the data is collected and processed by scraper.py, setup runs it through the reccomendation script, then saves it a neat and readable JSON tree for the frontend to use

## scraper.py

This script pulls information from different websites using a plugin called Beautiful Soup, then uses clustering to group them into groups based on similarity.

## reccommendations.py

This script populates the individual data points with lists of related articles, based on a version of KNN. The related articles are chosen from within the comparison articles's respective cluster.

## helpers.py

This file contains helper functions which accomplish a variety of tasks related to document scoring and classification. 

#### All code in this project is my own individual work, aside from certain imported modules ####
