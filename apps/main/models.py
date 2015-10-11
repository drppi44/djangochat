from django.db import models
from django.db.models.signals import post_save


class Message(models.Model):
    name = models.CharField(max_length=55)
    text = models.TextField()
    datetime = models.DateTimeField(auto_created=True)

    def __unicode__(self):
        return unicode('%s - %s' % (self.name, self.text[:15]))

    @staticmethod
    def log_message(sender, instance, created, **kwargs):
        with open('message_logs.dat', 'a') as p:
            print "%s: %s" % (instance.name, instance.text)
            p.write(str(instance)+'\n')

post_save.connect(Message.log_message, sender=Message)
