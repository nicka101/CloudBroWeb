from django.shortcuts import render
from django.http import HttpResponse
from twitch.models import StreamPreference, Stream
from twitch import api
from urllib.error import HTTPError
import json


def get_first_available_stream():
    streams = get_available_streams()
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
            return []
        streams = []
        for stream in res['streams']:
            streams.append(Stream(
                stream['channel']['name'],
                stream['channel']['display_name'],
                stream['viewers'],
                stream['channel']['status'],
                stream['game']
            ))
    except HTTPError:
        return []
    streams_ordered = []
    for user in pref:
        res = [stream for stream in streams if stream.username == user.username]
        if len(res) is 1:
            streams_ordered.append(res[0])
    return streams_ordered


def available_streams(request):
    streams = get_available_streams()
    return HttpResponse('{ "streams": ' + json.dumps([stream.__dict__ for stream in streams]) + ' }', 'application/json')