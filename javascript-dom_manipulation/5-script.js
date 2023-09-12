const click = document.querySelector('#update_header');
click.addEventListener('click', headerUpdate);

function headerUpdate () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
}
