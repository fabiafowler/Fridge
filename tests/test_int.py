import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Food

# Set test variables for test food name
test_admin_food_name = "foodtest"

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DATABASE'))
        app.config['SECRET_KEY'] = getenv('SKEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/Users/fabiafowler/Documents/WebDriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestAddToFridge(TestBase):

    def test_addtofridge(self):
        """
        Test that a user can add a food item to the fridhe using the food form
        if all fields are filled out correctly, and that they will be 
        redirected to the home page
        """

        # Click fridge menu link
        self.driver.find_element_by_xpath("/html/body/a[3]").click()
        time.sleep(1)

        # Fill in food name and click
        self.driver.find_element_by_xpath('//*[@id="food_name"]').send_keys(test_admin_food_name)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to login page
        assert url_for('home') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)