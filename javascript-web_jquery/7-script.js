$.ajax({
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    type: 'GET',
    dataType: 'json',
    success: function (data) {
        $('#character').text(data.name);
    }
});
