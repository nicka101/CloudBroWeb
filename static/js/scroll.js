$(function() {
    $(document).on('click', 'a.slide-to', function(e) {
        e.preventDefault();
        scrollTo($(this).attr('href'));
        return false;
    });
        var animMaxCount = 2;
    var timeOut;
    var offsetList = { 'headerStart': 0 };
    var state = { 'noSubnav': false, 'fancyScrolling': false, 'lastScroll': 0, scrollDirection : 1, 'activeElement': new Object() };

    function scrollTo(id) {
        state.fancyScrolling = true;
        $('html, body').animate({
            scrollTop: $(id).offset().top
        }, 900, function(){
            state.fancyScrolling = false;
            
        } );
    }
    
});
