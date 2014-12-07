from django.db import models
from ordered_model.models import OrderedModel


class StreamPreference(OrderedModel):
    username = models.CharField('Twitch Username', max_length=100, unique=True)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return "%s at position %d" % (self.username, self.order)
