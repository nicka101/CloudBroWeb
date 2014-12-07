
var mobile = {
    is_mobile: false,
    init: function () {
        this.is_mobile = (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent))?true:false;
    }
};

$(document).ready(function () {
    $('a.article-post').hover(function(){
        var self = $(this),
        priorText = self.text();
        self.text(self.data('content'));
        self.data('content',priorText);
    });
    
    
    $('div.article-post').click(function(){
        if($(this).hasClass('active')){
            var self = $(this),
            content = self.find('.post-content');
            self.toggleClass('active');
            content.slideToggle("fast");
        } else {
            $('div.article-post.active').find('.post-content').stop().slideToggle("fast");
            $('div.article-post.active').removeClass('active');
            var self = $(this),
            content = self.find('.post-content');
            self.toggleClass('active');
            content.stop().animate({opacity:'toggle',height:'toggle'},{duration:200});
        }
    });
    setTimeout(function() {
        var i = 0;
        $('.article-post').each(function () {
            var delay = 200 * i;
            console.log(delay);
            var self = $(this);
            setTimeout(function() {
                self.animate({marginTop:0,opacity:1},{duration:200});
            },delay);
            i++;
        });
    },600);
    mobile.init();
});