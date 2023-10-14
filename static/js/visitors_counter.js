$(document).ready(function () {
    var csrftoken = getCookie('csrftoken');

    $.ajax({
        url: '/record-visit/',
        type: 'POST',
        dataType: 'json',
        headers: { "X-CSRFToken": csrftoken },
        success: function (data) {
            if (data.status === 'active_session') {
                // console.log('User has an active session.');
            }else if (data.status === 'success') {
                // console.log('Visit recorded successfully.');
            } else {
                console.error('Error recording visit.');
            }
        },
        error: function () {
            console.error('AJAX request failed.');
        }
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            // console.log('cookies')
            // console.log(cookies)
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
