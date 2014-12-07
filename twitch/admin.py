from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from twitch.models import StreamPreference


class StreamPreferenceAdmin(OrderedModelAdmin):
    list_display = ('username', 'move_up_down_links')

admin.site.register(StreamPreference, StreamPreferenceAdmin)
