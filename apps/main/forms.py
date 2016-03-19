from datetime import datetime
from .models import Message
from django import forms


class MessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['file'].required = False

    class Meta:
        model = Message
        fields = ('name', 'text', 'file')

    def save(self, *args, **kwargs):
        message = super(MessageForm, self).save(commit=False)
        message.datetime = datetime.now()
        message.save()
        return message
