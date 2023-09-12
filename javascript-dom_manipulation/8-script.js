document.addEventListener('DOMContentLoaded', (event) => {
  const helloId = document.getElementById('hello');
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      const hello = data.hello;
      helloId.textContent = hello;
    });
});
