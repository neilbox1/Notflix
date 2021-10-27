//TMDB api

const API_KEY = 'api_key=870c39df7d9874056daa00e472d1533f';
const BASE_URL = 'https://api.themoviedb.org/3';
const API_URL = BASE_URL + '/discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc&'+API_KEY;
const IMG_URL = 'https://image.tmdb.org/t/p/w500';
const searchURL = BASE_URL + '/search/movie?' + API_KEY;

const main = document.getElementById('main');
const form = document.getElementById('form');
const search = document.getElementById('search');

getAnime(API_URL);

function getAnime(url){
    fetch(url).then(res => res.json()).then(data =>{
        console.log(data.results);
        showAnime(data.results);
    })
}

function showAnime(data) {
    main.innerHTML = '';

    data.forEach(anime => {
        const {title, poster_path, vote_average, overview} = anime;
        const animeEL = document.createElement('div');
        animeEL.classList.add('anime');
        animeEL.innerHTML = `
             <img src="${IMG_URL+poster_path}" alt="${title}">
            
            <div class="anime-info">
                <h3>${title}</h3>
                <span class="${getColor(vote_average)}">${vote_average}</span>
            </div>

            <div class="overview">
                ${overview}
            </div>
        `
        main.appendChild(animeEL);
    })
}

function getColor(vote){
    if(vote >=8){
        return 'green'
    }else if(vote >=5){
        return 'orange'
    }else{
        return 'red'
    }
}

form.addEventListener('submit', (e) =>{
    e.preventDefault();
    const searchTerm = search.value;

    if(searchTerm){
        getAnime(searchURL+'&query='+searchTerm)
    }else{
        getAnime(API_URL);
    }
})