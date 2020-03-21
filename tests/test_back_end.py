import unittest

from flask import abort, url_for
from flask_testing import TestCase

from application import app, db
from application.models import Food, Recipe

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@34.89.61.95:3306/fridge_app")
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        test = Food(name="potato")

        # create test non-admin user
        test2 = Food(name="broccoli")

        # save users to database
        db.session.add(test)
        db.session.add(test2)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
