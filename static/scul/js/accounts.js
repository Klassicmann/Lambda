$(document).ready(function () {

    $('#change-pro-img').on('click', function () {
        $('#upd-img').show(500);
    });

    var account_type = $('#account_type').text()
    if (account_type == 'Teacher') {
        $('#condi').show();

    }

    $('#course-cover').hover(function () {
        $('#course-cover img').css({ 'transform': 'scale(1.2)' });
    }, function () {
        $('#course-cover img').css({ 'transform': 'scale(1)' });
    });



    // $('#user-check h3:nth-child(5)').addClass('users-warn');


});
