from django.db import models
from ordered_model.models import OrderedModel
from collections import namedtuple


class StreamPreference(OrderedModel):
    username = models.CharField('Twitch Username', max_length=100, unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return "%s at position %d" % (self.username, self.order)


Stream = namedtuple('stream', ['username', 'display_name', 'viewer_count', 'status', 'game'])