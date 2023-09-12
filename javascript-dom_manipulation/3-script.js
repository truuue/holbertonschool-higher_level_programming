const click = document.querySelector('#toggle_header');
click.addEventListener('click', updateColor);

function updateColor () {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
    header.classList.add('green');
  } else if (header.classList.contains('green')) {
    header.classList.remove('green');
    header.classList.add('red');
  } else {
    header.classList.add('red');
  }
}
