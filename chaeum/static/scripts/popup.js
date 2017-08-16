function popupSwap(type) {
    $('.popup_frame > div[class*="popup_"]').hide();
    $('.popup_frame > div[class="popup_'+type+'"]').show();
}

function popupToggle() {
    $('.bg_popup').height($('body').height());
    $('.bg_popup').fadeToggle();

    var screenWidth = $(window).width();
    var left = (screenWidth - $('.popup_frame').width()) / 2;
    $('.popup_frame').css('left', left/16.0+'em');
    $('.popup_frame').fadeToggle();
}

$(function() {
    // popup close
    $('.popup_frame .close, .bg_popup').on('click', function(e) {
        popupToggle();
        e.preventDefault();
    });
});