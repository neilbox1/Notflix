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
        const {title, poster_path, vote_average, overview, id} = movie;
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
            <center><p><a onclick="movieSelected('${id}')" class="btn btn-primary" href="detail" role="button">View details &raquo;</a></p></center> 
        `
        main.appendChild(movieEL);
    })
}
function movieSelected(id2){
    axios.get('https://api.themoviedb.org/3/movie/' +id2 +'/external_ids?' + API_KEY)
     .then((response) => {
         console.log(response);


        result = response.data.imdb_id;
        console.log(result);

     })
    sessionStorage.setItem('movieId',result);
    window.location = 'detail';
    return false;
}


function getDetails(){
    let movieId = sessionStorage.getItem('movieId');

    axios.get('http://www.omdbapi.com/?i='+movieId + '&apikey=9be27fce')
     .then((response) => {
         console.log(response);
        let movie = response.data;


        let output = `
            <div class="detail">
                <div class="col-md-4">
                </div>
                    <img src="${movie.Poster}" class="thumbnail">
                <div class="col-md-8">
                    <h2>${movie.Title}</h2>
                    <ul class="list-group">
                        <li class="list-group-item"><strong>Genre:</strong> ${movie.Genre}</li>
                        <li class="list-group-item"><strong>Released:</strong> ${movie.Released}</li>
                        <li class="list-group-item"><strong>Director:</strong> ${movie.Director}</li>
                        <li class="list-group-item"><strong>Writer:</strong> ${movie.Writer}</li>
                        <li class="list-group-item"><strong>Actors:</strong> ${movie.Actors}</li>
                    </ul>
                </div>
            </div>
            <div class="detail">
                <h3>Plot</h3>
                ${movie.Plot}
                <hr>
                <a href="http://imdb.com/title/${movie.imdbID}" target="_blank" class="btn btn-primary">View IMDB</a>
                <a href="index.html" class="btn btn-default">Go Back To Search</a>
            </div>
        
        `;

        $('#movie').html(output);
     })
     .catch((err) => {
         console.log(err);
     });
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