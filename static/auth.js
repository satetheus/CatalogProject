
function start() {
    gapi.load('auth2', function () {
        auth2 = gapi.auth2.init({
            client_id: '506926343220-t1f403simfav5cbr8i4udls4l3mr0d82.apps.googleusercontent.com'
        });
    });
}