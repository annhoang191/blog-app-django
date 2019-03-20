$( document ).ready(function() {
  $('#comment-form').on('submit', function(e){
    var id = window.location.href.split('/')[4]
    e.preventDefault();
    $.ajax({
      url: `/blog/${id}`,
      type: 'POST',
      data: {content: $('#id_content').val()},
      beforeSend: function(xhr, settings) {
        console.log("Before Send");
        $.ajaxSettings.beforeSend(xhr, settings);
      },
      success: function(json){
        $('#id_content').val('')
        console.log(json)
        $('#comment-section').prepend("<article class='row'><div class='col-md-10 col-sm-10'>" +
          "<div class='panel panel-default arrow left'><div class='panel-body'>" +
          "<header class='text-left'><div class='comment-user'><i class='fa fa-user'></i>"
          + json.author + "said on "
          + json.created +
          "</header><div class='comment-post'><p>"
          + json.content +
          "</p></div></div></div></div></article>")
      }
    })
  })
})

$(function() {
  // This function gets cookie with a given name
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  /*
  The functions below will create a header with csrftoken
  */

  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
  }

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });

});
