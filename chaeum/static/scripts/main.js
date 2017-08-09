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
});
