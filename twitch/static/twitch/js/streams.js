var Streams = (function() {
	var timer = null;
	var live = false;
	var REGEX = new RegExp('\{username\}', 'gi');
	var HREF_CLASS = 'stream-href';
	var LONG_TEXT_CLASS = 'stream-text-long';
	var SHORT_TEXT_CLASS = 'stream-text-short';
	var STREAM_EMBED_CLASS = 'stream-embed';

    var HREF_TEMPLATE = 'http://www.twitch.tv/{username}';
	var LONG_TEXT_TEMPLATE = '{username} is currently live!';
	var SHORT_TEXT_TEMPLATE = 'Watch {username} live!';
	var STREAM_EMBED_TEMPLATE = '<object type="application/x-shockwave-flash" width="100%" height="100%" id="live_embed_player_flash" data="//www-cdn.jtvnw.net/swflibs/TwitchPlayer.swf" bgcolor="#000000"><param name="allowFullScreen" value="true" /><param name="allowScriptAccess" value="always" /><param name="allowNetworking" value="all" /><param name="movie" value="//www-cdn.jtvnw.net/swflibs/TwitchPlayer.swf" /><param name="flashvars" value="hostname=www.twitch.tv&channel={username}&auto_play=true&start_volume=25&embed=1" /></object>';

	window.addEventListener('load', function(){
	    autoUpdate(true);
	    updateInternal();
	}, false);

	var processResponse = function(json){
	    try {
	        var e = document.getElementById('stream-viewer');
	        if(json.streams.length > 0){
	            if(live) return;
	            live = true;
	            var stream = json.streams[0];
	            var hrefs = e.getElementsByClassName(HREF_CLASS);
	            for(var i = 0; i < hrefs.length; i++){
	                hrefs[i].href = HREF_TEMPLATE.replace(REGEX, stream.username);
	            }
	            var lt = e.getElementsByClassName(LONG_TEXT_CLASS);
	            for(var i = 0; i < lt.length; i++){
	                lt[i].innerHTML = LONG_TEXT_TEMPLATE.replace(REGEX, stream.display_name);
	            }
	            var st = e.getElementsByClassName(SHORT_TEXT_CLASS);
	            for(var i = 0; i < st.length; i++){
	                st[i].innerHTML = SHORT_TEXT_TEMPLATE.replace(REGEX, stream.display_name);
	            }
	            var se = e.getElementsByClassName(STREAM_EMBED_CLASS);
	            for(var i = 0; i < se.length; i++){
	                se[i].innerHTML = STREAM_EMBED_TEMPLATE.replace(REGEX, stream.username);
	            }
	            if(e.firstElementChild.classList.contains('offline')) e.firstElementChild.classList.remove('offline');
	        } else {
	            if(!e.firstElementChild.classList.contains('offline')) e.firstElementChild.classList.add('offline');
	        }
	    } catch(e){
	        console.warn("Stream status update in invalid format. This may be a hijacking");
	    }
	};

	var autoUpdate = function(active){
        if(active){
            if(timer == null) setInterval(updateInternal, 10000);
        } else if(timer != null) {
            clearInterval(timer);
            timer = null;
        }
	};

	var updateInternal = function(){
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
                    autoUpdate(false);
                    return;
                }
                processResponse(responseObject);
            }
        };
        request.open("GET", "/twitch/live_streams");
        request.setRequestHeader("Accept", "application/json");
        request.send();
	};

	//Public methods
    return {
        update: function(){
            updateInternal();
        },

        autoupdate: function(active){
            autoUpdate(active);
        }
    }
})();