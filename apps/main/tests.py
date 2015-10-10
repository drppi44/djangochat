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

    def test_home_pagE_has_logout_link(self):
        """home page has logout link if logged in"""
        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('home'))

        self.assertIn('logout', response.content)
