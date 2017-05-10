import unittest

from flask import abort, url_for
from flask_testing import TestCase

from app import create_app, db
from app.models import Department, Employee, Role

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
