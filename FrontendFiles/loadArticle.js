"use strict";

fetch("./bakedData.json").then(function(response){
    return response.json();
}).then(function(data){
    var articleID = parent.document.URL.substring(parent.document.URL.indexOf('?')+4, parent.document.URL.length);

    document.getElementById("main-title").innerHTML = data[articleID].title;
    document.getElementById("main-content").innerHTML = data[articleID].content;

    var relatedArticles = data[articleID].related;

    for(var i in relatedArticles){
        var titleID = relatedArticles[i.toString()].id
        document.getElementById("suggestion"+i.toString()).innerHTML = data[titleID.toString()].title;
        var link = document.getElementById("a"+i.toString());
        link.setAttribute("href", "./article.html?id="+titleID.toLocaleString());
    }
})