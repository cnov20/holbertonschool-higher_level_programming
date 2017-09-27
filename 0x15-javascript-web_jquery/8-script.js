const movieList = $('ul#list_movies');
const url = 'https://swapi.co/api/films?format=json';

$(function () {
  $.get(url, function (data, textStatus) {
    $.each(data.results, function (key, val) {
      let filmTitle = val.title;
      movieList.append('<li>' + filmTitle + '</li>');
    });
  });
});
