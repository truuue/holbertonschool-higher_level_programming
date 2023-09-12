const click = document.querySelector('#red_header');
click.addEventListener('click', updateColor);

function updateColor () {
  const header = document.querySelector('header');
  header.classList.add('red');
}
