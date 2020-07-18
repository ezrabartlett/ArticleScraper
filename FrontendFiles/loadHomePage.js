"use strict";

fetch("./bakedData.json").then(function(response){
    return response.json();
}).then(function(data){
    console.log(data);
    var articleNum = Object.keys(data).length;
    for(var i = 0; i<5; i++){
        var titleID = Math.floor(Math.random()*articleNum)
        document.getElementById("title"+i.toString()).innerHTML = data[titleID.toString()].title;
        var link = document.getElementById("a"+i.toString());
        link.setAttribute("href", "./article.html?id="+titleID.toLocaleString());
    }
})