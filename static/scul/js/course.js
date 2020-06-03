$(document).ready(function () {

    $('.course-middle').html();


    $('#tab-1').on('click', function () {
        $('#koko').show();
        $('.documents').hide();

        $('.course-middle .nav-tabs a:first-child').addClass('active');
        $('.course-middle .nav-tabs a:last-child').removeClass('active');
    });
    $('#tab-2').on('click', function () {
        $('.documents').show();
        $('#koko').hide();
        $('.course-middle .nav-tabs a:first-child').removeClass('active');

        $('.course-middle .nav-tabs a:last-child').addClass('active');
    });

    $("textarea").attr({
        "rows": "4",
        "cols": "15"
    });



    $('.thumbnail-videos  a').addClass('disabled');

    $('.course-middle a:first-child').on('click', function () {


        $('.thumbnail-videos  a').removeClass('disabled');
    });



        // var vid1 = $('#vid').html();
        // var titl1 = $('.titl1').html();

        // var vid2 = $('#mid-vid');
        // var titlx = $('#mid-vid-title');

        // vid2.html(vid1);
        // titlx.html(titl1);


   
    if ($(window).width() < 760) {
        $("#video-responsive").addClass('video-responsive');
        $("#mid-vid-text, #user-detail").removeClass('d-flex');


         //Books
        $("#book-authur, #book-covers").removeClass('col-3');
        $(".book-desc").removeClass('col-6');

        
    }

   


    


});

