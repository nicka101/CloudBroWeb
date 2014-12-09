from django.shortcuts import render
from twitch.models import StreamPreference, Stream
from twitch import api
from urllib.error import HTTPError


def get_first_available_stream():
    pref = StreamPreference.objects.all()
    for user in pref:
        try:
            res = api.get_stream(user.username)
            if res['stream'] is None:  # Stream offline
                continue
            return Stream(user.username,
                          res['stream']['channel']['display_name'],
                          res['stream']['viewers'],
                          res['stream']['channel']['status'],
                          res['stream']['game']
                          )
        except HTTPError:
            continue
    return None

