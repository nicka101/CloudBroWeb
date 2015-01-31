from django.shortcuts import render
from django.http import HttpResponse
from twitch.models import StreamPreference, Stream
from twitch import api
from urllib.error import HTTPError
import json


def get_first_available_stream():
    streams = get_available_streams()
    if streams is None:
        return None
    pref = StreamPreference.objects.all()
    for user in pref:
        res = [stream for stream in streams if stream.username == user.username]
        if len(res) is 1:
            return res[0]
    return None

def get_available_streams():
    pref = StreamPreference.objects.all()
    channels = ",".join(user.username for user in pref)
    try:
        res = api.get_streams(channel=channels)
        if res['streams'] is None:
            return None
        streams = []
        for stream in res['streams']:
            streams.append(Stream(
                stream['channel']['name'],
                stream['channel']['display_name'],
                stream['viewers'],
                stream['channel']['status'],
                stream['game']
            ))
        return streams
    except HTTPError:
        return None


def available_streams(request):
    stream = get_first_available_stream()
    if stream is None:
        return HttpResponse('{ "stream": null }', 'application/json')
    return HttpResponse('{ "stream": ' + json.dumps(stream.__dict__) + ' }', 'application/json')