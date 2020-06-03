$(document).ready(function () {
    $('#material').hover(function () {
        $('#material ul').toggle(1000);
    });
    $('#material1').hover(function () {
        $('#material1 ul').toggle(1000);
    });

    $("#img-a").on('click', function(){
        $("#m-sidebar").toggle(3000);
    });


});

