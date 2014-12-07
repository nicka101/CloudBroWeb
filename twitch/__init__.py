from urllib.request import Request, urlopen
from urllib.parse import quote, urlencode
from urllib.error import HTTPError
from json import JSONDecoder


_baseurl = "https://api.twitch.tv/kraken"
_apiversionheader = "application/vnd.twitchtv.v2+json"


class TwitchAPI(object):
    def __init__(self, client_id):
        self.client_id = client_id
        self.decoder = JSONDecoder()

    def _perform_request(self, path):
        req = Request(_baseurl + path, None, {'Accept': _apiversionheader, 'Client-ID': self.client_id})
        return self.decoder.decode(urlopen(req))

    @staticmethod
    def _build_qs(limit=25, offset=0, hls=False, embeddable=False, channel=None, game=None, broadcasts=False, q=None, period='week'):
        query = {}
        if game is not None:
            query['game'] = game
        if channel is not None:
            query['channel'] = channel
        if limit is not 25:
            if limit > 100 or limit <= 0:
                raise ValueError('limit must be in the range 1-100 (inclusive)')
            query['limit'] = limit
        if offset is not 0:
            if offset < 0:
                raise ValueError('offset cannot be negative')
            query['offset'] = offset
        if embeddable:
            query['embeddable'] = 'true'
        if hls:
            query['hls'] = 'true'
        if broadcasts:
            query['broadcasts'] = 'true'
        if q is not None:
            query['q'] = q
        if period is not 'week':
            if period not in ('week', 'month', 'all'):
                raise ValueError('Invalid option for period. Valid choices are "week", "month" and "all"')
        return urlencode(query)

    def get_streams(self, game=None, channel=None, limit=25, offset=0, embeddable=False, hls=False):
        query_string = TwitchAPI._build_qs(limit, offset, hls, embeddable, channel, game)
        if query_string is not '':
            return self._perform_request('/streams?' + query_string)
        return self._perform_request('/streams')

    def get_stream(self, channel_name):
        return self._perform_request('/stream/' + quote(channel_name, None))

    def get_featured_streams(self, limit=25, offset=0, hls=False):
        query_string = TwitchAPI._build_qs(limit, offset, hls)
        if query_string is not '':
            return self._perform_request('/streams/featured?' + query_string)
        return self._perform_request('/streams/featured')

    def get_streams_summary(self, limit=25, offset=0, hls=False):
        query_string = TwitchAPI._build_qs(limit, offset, hls)
        if query_string is not '':
            return self._perform_request('/streams/summary?' + query_string)
        return self._perform_request('/streams/summary')

    def get_channel(self, channel_name):
        return self._perform_request('/channel/' + quote(channel_name, None))

    def get_channel_videos(self, channel_name, limit=10, offset=0, broadcasts=False):
        query_string = TwitchAPI._build_qs(limit, offset, broadcasts=broadcasts)
        if query_string is not '':
            return self._perform_request('/channels/' + quote(channel_name, None) + '/videos?' + query_string)
        return self._perform_request('/channels/' + quote(channel_name, None) + '/videos')

    def get_channel_followers(self, channel_name, limit=25, offset=0):
        query_string = TwitchAPI._build_qs(limit, offset)
        if query_string is not '':
            return self._perform_request('/channels/' + quote(channel_name, None) + '/follows?' + query_string)
        return self._perform_request('/channels/' + quote(channel_name, None) + '/follows')

    def get_chat_emoticons(self):
        return self._perform_request('/chat/emoticons')

    def get_user_follows(self, username, limit=25, offset=0):
        query_string = TwitchAPI._build_qs(limit, offset)
        if query_string is not '':
            return self._perform_request('/users/' + quote(username, None) + '/follows/channels?' + query_string)
        return self._perform_request('/users/' + quote(username, None) + '/follows/channels')

    def does_user_follow_channel(self, username, channel_name):
        req = Request(_baseurl + '/users/' + quote(username, None) + '/follows/channels/' + quote(channel_name, None),
                      None,
                      {'Accept': _apiversionheader, 'Client-ID': self.client_id},
                      method='HEAD'
                      )
        try:
            return urlopen(req).status is 200
        except HTTPError:
            return False

    def get_top_games(self, limit=25, offset=0, hls=False):
        query_string = TwitchAPI._build_qs(limit, offset, hls)
        if query_string is not '':
            return self._perform_request('/games/top?' + query_string)
        return self._perform_request('/games/top')

    def search_streams(self, query, limit=25, offset=0):
        return self._perform_request('/search/streams?' + TwitchAPI._build_qs(limit, offset, q=query))

    def search_games(self, query, limit=25, offset=0):
        return self._perform_request('/search/games?' + TwitchAPI._build_qs(limit, offset, q=query))

    def get_teams(self, limit=25, offset=0):
        query_string = TwitchAPI._build_qs(limit, offset)
        if query_string is not '':
            return self._perform_request('/teams?' + query_string)
        return self._perform_request('/teams')

    def get_team(self, team_name):
        return self._perform_request('/teams/' + quote(team_name, None))

    def get_user(self, username):
        return self._perform_request('/users/' + quote(username, None))

    def get_video(self, video_id):
        return self._perform_request('/videos/' + quote(video_id, None))

    def get_top_videos(self, limit=10, offset=0, game=None, period="week"):
        query_string = TwitchAPI._build_qs(limit, offset, game=game, period=period)
        if query_string is not '':
            return self._perform_request('/videos/top?' + query_string)
        return self._perform_request('/videos/top')