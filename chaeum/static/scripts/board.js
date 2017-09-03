$(function() {
    // board write button
    $('.search_write button.write').on('click', function(e) {
        popupSwap('board');
        popupToggle();
        e.preventDefault();
    });
});