from datetime import datetime
from .models import Message
from django import forms


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('name', 'text')

    def save(self, *args, **kwargs):
        message = super(MessageForm, self).save(commit=False)
        message.datetime = datetime.now()
        message.save()
        return message
