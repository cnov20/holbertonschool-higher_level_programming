const header = $('header.green');
const toggleHeader = $('div#toggle_header');
toggleHeader.click(function () {
  header.toggleClass('red green');
});
