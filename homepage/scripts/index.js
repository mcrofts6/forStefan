$(function() {
    // update the time every n seconds
    window.setInterval(function() {
        $('.browser-time').text('The current browser time is ' + new Date());
    }, 1000);

    // update button
    $('#server-time-button').click(function() {
        $('.server-time').load('/homepage/index.gettime');
    });
});

