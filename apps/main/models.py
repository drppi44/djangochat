from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=55)
    text = models.TextField()
    datetime = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return unicode('%s - %s' % (self.title, self.text[:15]))
