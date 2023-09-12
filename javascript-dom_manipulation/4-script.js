const click = document.querySelector('#add_item');
click.addEventListener('click', addList);

function addList () {
  const myList = document.querySelector('.my_list');
  const newList = document.createElement('li');
  newList.textContent = 'Item';
  myList.appendChild(newList);
}
