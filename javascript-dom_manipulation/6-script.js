const characterId = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const characterName = data.name;
    characterId.textContent = characterName;
  });
