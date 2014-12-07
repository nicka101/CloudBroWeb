$(function(){
	function main() {
	    var currentYear = (new Date).getFullYear();
		  $(document).ready(function() {
		  $("#year").text( (new Date).getFullYear() );
		  });
	    if($(window).width() < 768)
	    {   
	        
	    	$( ".dropdown-toggle" ).unbind('click').bind("click",function() {

	  		
		        if ($(this).next( ".dropdown-menu" ).hasClass("open")){
		        	$( this ).next( ".dropdown-menu" ).slideUp();
			        $(this).next( ".dropdown-menu" ).removeClass("open");

				}
				else{
					$( this ).next( ".dropdown-menu" ).slideDown();
			        $(this).next( ".dropdown-menu" ).addClass("open");
				}
		  		$('.dropdown-toggle').not(this).each(function(){
				     $(this).next( ".dropdown-menu" ).slideUp();
				     $(this).next( ".dropdown-menu" ).removeClass("open");
		     
		     	});
	        
			});
	    }
	    else
	    {
       	    $( ".dropdown-toggle" ).unbind('click');
            $( ".dropdown-menu" ).removeAttr('style');
	    }

	};
	//initialize
	main();

	//call when the page resizes.
	var az;
	$(window).resize(function() {
	    clearTimeout(az);
	    id = setTimeout(main, 500);
	    
	});

});