"""
Module provides UI tests for https://www.metric-conversions.org/
- Test for converting Celsius to Fahrenheit temperature;
- Test for converting meters to feet;
- Test for converting ounces to grams;
"""


from selenium import webdriver
import unittest
from webdriver_manager.firefox import GeckoDriverManager
import time


DRIVER = webdriver.Firefox(executable_path=GeckoDriverManager().install())
URL = 'https://www.metric-conversions.org/'


class TestCelsiusToFahrenheit(unittest.TestCase):
    """
    Test celsius to fahrenheit conversion
    """
    def setUp(self):
        self.url = URL
        self.driver = DRIVER
        self.driver.set_window_size(1120, 550)
        self.correct_data = '5°C= 41.00000°F'
        self.input_data = 5

    def test_celsius_to_fahrenheit(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('queryFrom').send_keys('Celsius')
        time.sleep(2)
        self.driver.find_element_by_id('queryTo').send_keys('Fahrenheit')
        time.sleep(2)
        self.driver.find_element_by_class_name('argument').send_keys(5)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="results"]/ol/li/div/a[2]').click()
        time.sleep(2)
        answer = self.driver.find_element_by_id('answer')
        self.assertEqual(answer.text, self.correct_data)


class TestMetersToFeet(unittest.TestCase):
    """
    Tests conversion meters to feet
    """
    def setUp(self) -> None:
        self.url = URL
        self.driver = DRIVER
        self.driver.set_window_size(1120, 550)
        self.correct_data = '5m= 16ft 4.850394in'
        self.input_data = 5

    def test_meters_to_feet(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('queryFrom').send_keys('Meters')
        time.sleep(2)
        self.driver.find_element_by_id('queryTo').send_keys('Feet')
        time.sleep(2)
        self.driver.find_element_by_class_name('argument').send_keys(5)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="results"]/ol/li/div/a[2]').click()
        time.sleep(2)
        answer = self.driver.find_element_by_id('answer')
        self.assertEqual(answer.text, self.correct_data)


class TestOuncesToGrams(unittest.TestCase):
    """
    Tests conversion ounces to grams
    """
    def setUp(self) -> None:
        self.url = URL
        self.driver = DRIVER
        self.driver.set_window_size(1120, 550)
        self.correct_data = '5oz= 141.7476g'
        self.input_data = 5

    def test_meters_to_feet(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id('queryFrom').send_keys('Ounces')
        time.sleep(2)
        self.driver.find_element_by_id('queryTo').send_keys('Grams')
        time.sleep(2)
        self.driver.find_element_by_class_name('argument').send_keys(5)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="results"]/ol/li/div/a[2]').click()
        time.sleep(2)
        answer = self.driver.find_element_by_id('answer')
        self.assertEqual(answer.text, self.correct_data)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
