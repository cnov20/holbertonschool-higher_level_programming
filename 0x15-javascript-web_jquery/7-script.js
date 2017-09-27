const character = $('div#character');
const url = 'https://swapi.co/api/people/5/?format=json';

$(function () {
  $.get(url, function (data, textStatus) {
    character.replaceWith(data.name);
  });
});
