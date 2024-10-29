import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import data
import locators
import method
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities



class TestUrbanRoutes:

    driver = None

    @classmethod
    #def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
     #   from selenium.webdriver import DesiredCapabilities
      #  capabilities = DesiredCapabilities.CHROME
       # capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        #cls.driver = webdriver.Chrome()

    def setup_class(cls):
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        service = Service()
        cls.driver = webdriver.Chrome(service=service, options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(2)
        routes_page = method.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_call_taxi(self):
        self.driver.get(data.urban_routes_url)
        time.sleep(2)
        routes_page = method.UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_from(address_from)
        routes_page.set_to(address_to)
        routes_page.request_taxi()
        routes_page.pick_comfort()
        routes_page.set_phone_number()
        routes_page.set_payment()
        routes_page.set_message()
        routes_page.set_requirements()
        routes_page.call_taxi()
        routes_page.wait_driver_details()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
