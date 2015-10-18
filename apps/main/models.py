import os
from django.db import models
from django.db.models.signals import post_save


class Message(models.Model):
    name = models.CharField(max_length=55)
    text = models.TextField()
    datetime = models.DateTimeField(auto_created=True)
    file = models.FileField(upload_to='files/', null=True)

    def __unicode__(self):
        return unicode('%s - %s' % (self.name, self.text[:15]))

    @staticmethod
    def log_message(sender, instance, created, **kwargs):
        with open('message_logs.dat', 'a') as p:
            p.write(str(instance)+'\n')

    def filename(self):
        return os.path.basename(self.file.name)

post_save.connect(Message.log_message, sender=Message)
