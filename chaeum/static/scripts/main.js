$(function() {
    // sub navigation bar on/off slide
    $('header nav .sub_menu_wrap').click(function() {
        $('header subnav').slideToggle();
    });

    // search focus in/out
    $('header .top .search input').focusin(function() {
        // focus in
        $('header .top .search').css('border-color', '#ff531d');
        $('header .top .search .auto_comp').toggle();
    }).focusout(function() {
        // focus out
        $('header .top .search').css('border-color', '#563540');
        $('header .top .search .auto_comp').toggle();
    });

    // top sign in button
    $('#top_signin').on('click', function(e) {
        popupSwap('signin');
        popupToggle();
        e.preventDefault();
    });

    // top sign up button
    $('#top_signup').on('click', function(e) {
        popupSwap('signup');
        popupToggle();
        e.preventDefault();
    });
});
