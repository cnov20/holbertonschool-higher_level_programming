$(document).ready(function () {
  const addItem = $('div#add_item');
  const removeItem = $('div#remove_item');
  const listItem = $('li');
  const newItem = '<li>New Item</li>';
  const clearList = $('div#clear_list');
  const myList = $('ul.my_list');

  addItem.on('click', function () {
    myList.append(newItem);
  });

  removeItem.on('click', function () {
    $('li:last-child');
    listItem.remove(listItem);
  });

  clearList.on('click', function () {
    myList.remove();
  });
});
