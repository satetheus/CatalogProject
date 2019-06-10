
function start() {
    gapi.load('auth2', function () {
        auth2 = gapi.auth2.init({
            client_id: '506926343220-t1f403simfav5cbr8i4udls4l3mr0d82.apps.googleusercontent.com'
        });
    });
}

function signInCallback(authResult) {
    if (authResult['code']) {
        $('#signinButton').attr('style', 'display: none');
        $.ajax({
            type: 'POST',
            url: '/gconnect?state='+STATE,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            contentType: 'application/octet-stream; charset=utf-8',
            success: function (result) {
                $('#result').html('Login Successful!</br>' + result + '</br>Redirecting...')
                setTimeout(function () {
                    window.location.href = "/catalog/";
                }, 2000);
            },
            processData: false,
            data: authResult['code']
        });
    } else {
        // handle error
        console.log('There was an error: ' + authResult['error']);
        $('#result').html('Failed to make a server-side call. Check your configuration and console.');

    }
}
