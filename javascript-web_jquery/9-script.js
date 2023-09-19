$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    dataType: 'json',
    success: function (greeting) {
      $('#hello').text(greeting.hello);
    }
});
