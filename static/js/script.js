//TMDB api

const API_KEY = 'api_key=870c39df7d9874056daa00e472d1533f';
const BASE_URL = 'https://api.themoviedb.org/3';
const API_URL = BASE_URL + '/discover/movie?sort_by=popularity.desc&'+API_KEY;
const IMG_URL = 'https://image.tmdb.org/t/p/w500';
const searchURL = BASE_URL + '/search/movie?' + API_KEY;

const main = document.getElementById('main');
const form = document.getElementById('form');
const search = document.getElementById('MovieSearch');

getMovie(API_URL);

function getMovie(url){
    fetch(url).then(res => res.json()).then(data =>{
        console.log(data.results);
        showMovie(data.results);
    })
}

function showMovie(data) {
    main.innerHTML = '';

    data.forEach(movie => {
        const {title, poster_path, vote_average, overview} = movie;
        const movieEL = document.createElement('div');
        movieEL.classList.add('movie');
        movieEL.innerHTML = `
             <img class="image" src="${IMG_URL+poster_path}" alt="${title}">
            
            <div class="movie-info">
                <h3>${title}</h3>
                <span class="${getColor(vote_average)}">${vote_average}</span>
            </div>

            <div class="overview">
                ${overview}
            </div>
            <center><p><a class="btn btn-primary" href="#" role="button">View details &raquo;</a></p></center>   
        `
        main.appendChild(movieEL);
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
        getMovie(searchURL+'&query='+searchTerm)
    }else{
        getMovie(API_URL);
    }
})