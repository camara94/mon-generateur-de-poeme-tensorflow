// contient les poèmes de certains auteurs, qui doivent être 
// gardés en mémoire même après affichage du graphique
var news_data;


var content = document.getElementById('text');
var bouton = document.getElementById('btn');

bouton.addEventListener('click', (e) => {
    /*var art = document.getElementById('url').value;
    var doc = document.getElementById('cont');
    var load = document.getElementById('load');*/
    e.preventDefault()
    var b = {'tag': content.value.toString()}
    var parent = document.getElementById('container');
    var image = document.createElement('img');
    image.setAttribute('class','image')
    image.src = 'images/loading.gif';

    

    parent.appendChild(image);
    let div = document.getElementById('poeme');
    if(image != null && div != null) {
        
        parent.removeChild(div)
    }
    var xhr = new XMLHttpRequest();
    xhr.addEventListener("progress", (e) => {
        if (e.lengthComputable) {    

            var percentComplete = e.loaded / e.total * 100;
            if (percentComplete>=100)
              parent.removeChild(image);   
          } 
    });

    xhr.onreadystatechange = () => { //Appelle une fonction au changement d'état.
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            display_poeme(xhr.responseText)
        }
    }
    
    xhr.open("GET", "http://localhost:5000/api/poemes?tag="+content.value);
    //xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(  );
})






function display_poeme(result) {
	news_data = result;

    let div = document.createElement('div');
    div.setAttribute('id', 'poeme');
    let contenu = document.createTextNode(news_data);
   

    let titre = document.createElement('h3');
    let text = document.createTextNode('Votre Super Poème')
    titre.style.fontSize = "20px";
    titre.style.fontWeight = "bold";
    titre.style.textDecoration = "underline";
    titre.style.textAlign = "center"
    titre.appendChild(text);

    div.appendChild(titre)
    div.appendChild(contenu)


    let parent = document.getElementById('container');
    parent.appendChild(div)
}

