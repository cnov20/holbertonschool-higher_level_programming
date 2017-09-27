const myList = $('ul.my_list');
const addItem = $('div#add_item');
addItem.click(function () {
  myList.append('<li>New item</li>');
});
