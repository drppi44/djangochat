import json
from apps.main.models import Message
from django.core import serializers
from .forms import MessageForm
from django.core.urlresolvers import reverse
from django.test import TestCase


class HomePageTest(TestCase):
    fixtures = ['users.json']

    def test_home_page_code_and_html(self):
        """200 code, index.html"""
        response = self.client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_message_form_in_context_if_logged_in(self):
        """logged in user response context has message form"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('home'))

        self.assertIsInstance(response.context['form'], MessageForm)

    def test_home_page_has_login_reg_links(self):
        """home page has links to login and registrating pages"""
        response = self.client.get(reverse('home'))

        self.assertIn('login', response.content)
        self.assertIn('registration', response.content)

    def test_home_page_has_logout_link(self):
        """home page has logout link if logged in"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('home'))

        self.assertIn('logout', response.content)


class AuthTest(TestCase):
    fixtures = ['users.json']

    def test_login_page_code_html(self):
        """200 code, login.html"""
        response = self.client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_registration_page_code_html(self):
        """200 code, login.html"""
        response = self.client.get(reverse('registration'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration.html')

    def test_login_page_has_login_form(self):
        """login page has login form content, context"""
        response = self.client.get(reverse('login'))

        self.assertTrue(response.context['form'])
        self.assertIn('form', response.content)
        self.assertIn('id_username', response.content)
        self.assertIn('id_password', response.content)

    def test_registration_page_has_login_form(self):
        """registration page has login form content, context"""
        response = self.client.get(reverse('registration'))

        self.assertTrue(response.context['form'])
        self.assertIn('form', response.content)
        self.assertIn('id_username', response.content)
        self.assertIn('id_password1', response.content)
        self.assertIn('id_password2', response.content)


class ChatTest(TestCase):
    fixtures = ['users.json', 'messages.json']

    def test_post_ajax_chat_add(self):
        """post to add message to chat in db(requires login)"""
        name = 'belyash'
        text = 'dasdasdas'

        self.client.login(username='admin', password='admin')
        response = self.client.post(reverse('chat-add'),
                                    {'name': name, 'text': text})

        message = Message.objects.last()

        self.assertEquals(message.name, name)
        self.assertEquals(message.text, text)
        self.assertEquals(json.loads(response.content), dict(success=True))

    def test_chat_get(self):
        """get messages ajax returns messages"""
        response = self.client.get(reverse('chat-get'))

        self.assertEquals(
            serializers.serialize('json', Message.objects.all()),
            response.content
        )
