import unittest

from django.test import TestCase, Client

from infotienda.models import Provincia

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class ProvinciaTest(TestCase):

    def setUp(self):
        Provincia.objects.create(nombre='Pichincha')
        Provincia.objects.create(nombre='Cotopaxi')
        Provincia.objects.create(nombre='Tungurahua')

    def test_string_representation(self):
        pichincha = Provincia.objects.get(nombre='Pichincha')
        cotopaxi = Provincia.objects.get(nombre='Cotopaxi')
        tungurahua = Provincia.objects.get(nombre='Tungurahua')

        self.assertEqual(pichincha.nombre, 'Pichincha')
        self.assertEqual(cotopaxi.nombre, 'Cotopaxi')
        self.assertEqual(tungurahua.nombre, 'Tungurahua')


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)


class SimpleTest1(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/privacidad/')
        self.assertEqual(response.status_code, 200)



class BusquedaTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        response = self.client.get('/busqueda/')

        self.assertEqual(response.status_code, 302)



class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % ('http://127.0.0.1:8000/admin', '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('david')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('D@vidpull0')
        self.selenium.find_element_by_xpath('//input[@value="Iniciar sesión"]').click()