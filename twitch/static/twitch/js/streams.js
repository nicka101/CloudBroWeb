var Streams = (function() {
	var timer = null;

	var init = function(){
	    timer = setInterval(update, 10000);
	};

	var processResponse = function(json){

	};

	//Public methods
    return {
        update: function(){
			var request = new XMLHttpRequest();
            request.ontimeout = function(){ console.warn("Stream status update timed out"); };
            request.onreadystatechange = function(){
            if(request.readyState == 4){
                if(request.status !== 200){
                    console.warn("Stream status update returned non-success code: " + request.status);
                    return;
                }
                try {
                    var responseObject = JSON.parse(request.responseText);
                }catch(e){
                    console.warn("Stream status update returned invalid JSON response");
                    return;
                }
                processResponse(responseObject);
            }
            };
            request.open("GET", "/twitch/live_streams");
            request.setRequestHeader("Accept", "application/json");
            request.send();
        },

        autoupdate: function(active){
            if(active){
                if(timer == null) setInterval(update, 10000);
            } else if(timer != null) {
                clearInterval(timer);
            }
        }
    }
})();