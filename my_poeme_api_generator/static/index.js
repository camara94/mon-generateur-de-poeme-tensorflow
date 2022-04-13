// contient les poèmes de certains auteurs, qui doivent être 
// gardés en mémoire même après affichage du graphique
var news_data;

// Palette de couleurs utilisée par tous les graphiques
var colors = ["#1D507A", "#2F6999", "#66A0D1", "#8FC0E9", "#4682B4"];

// Chargement des poèmes
$.ajax({
          url: "/api/words",
          success: display_news
});



function display_news(result) {
	news_data = result;
    display_wordcloud(news_data);
    display_all_articles();
}

var others = []
function display_wordcloud(news_data) {

    var data = [];
    var keywords = news_data["poeme"];
    
    for (i in keywords) {
        data.push({
            name: keywords[i]["name"],
            weight: keywords[i]["weight"],
            events: {
                click: function(event) {
                    var keyword = event.name;
                    display_articles_from_word(keyword, keywords);
                }
            }
        })
    }
    console.log("Voici les données formatées pour Highcharts :", typeof(data));
    console.log("Voici les données formatées pour Highcharts 2:", typeof([{'name': 'laby'}, {'name':'damaro'}]));
    //if(others.length>0)
    Highcharts.chart('nuage', {
        series: [{
            type: 'wordcloud',
            data: data.splice(keywords.length-300, keywords.length),
            name: 'Occurrences',
            colors: 
                colors,
            rotation: {
                from: -60,
                to: 60,
                orientations: 8
            },
        }],
        title: {
            text: 'Mots de bases : nuage de mots'
        },
        chart: {
            backgroundColor: 'None'
        }
    });
}

function display_all_articles() {
    var all_articles = []
    for (i = 0; i < news_data['poeme'].length; i++)
        all_articles.push(news_data['poeme']);
        console.log(all_articles)
    display_articles(all_articles);
}

function display_articles_from_word(word, articles) {
    for (i in articles['poeme']) {
        if (articles['poeme']['name'] == word) {
            articles = articles['poeme'];
            break;
        }
    }
    display_articles(articles);
};

function display_articles(articles) {
    var div = $("#tableauArticles").html("");
    div.append("<table></table");
    var tab = $("#tableauArticles table");
    for (i in articles) {
        var article = news_data['poeme'];
        var title = article[i]["name"];
        var source = article[i]["weight"];
        var url = article[i]["url"];
        var newLine = "<tr><td class='newspaper'>" + source + "</td><td><a target='_blank'href='" + url + "'>" + title + "</a></td></tr>"
        tab.append(newLine);
    }
}
