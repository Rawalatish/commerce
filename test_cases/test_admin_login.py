import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base_pages.Login_Admin_Page import Login_Admin_Page
from test_cases import conftest
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:
    # admin_page_url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    # username = "admin@yourstore.com"
    # password = "admin"
    # invalid_password = "invalid"

    # we defined above in the config so we will call it from there

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()

    logger = Log_Maker.log_gen()

    @pytest.mark.regression
    def test_title_verification(self):
        # self.logger.info("******** we are in Test 01 admin login class ******")
        # self.logger.info("******** verification of title ******")
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        exp_title = "nopCommerce demo store. Login"
        # self.driver.save_screenshot(r"C:\Users\HP\PycharmProjects\nopcommerce\screenshots")

        if act_title == exp_title:
            # self.logger.info("******** title matched ******")

            assert True
            self.driver.close()
        else:
            # self.driver.save_screenshot("C:\\Users\\HP\\PycharmProjects\\nopcommerce\\screenshots.png")
            self.driver.save_screenshot("..\\screenshots\\title_verification.png")
            # self.logger.info("******** title verification failed ******")

            self.driver.close()
            assert False


    # def test_valid_admin_login(self, setup):
    #     # self.driver = webdriver.Chrome()
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.password)
    #     self.admin_lp.click_login()
    #     # time.sleep(30)
    #     self.driver.save_screenshot("..\\screenshots\\valid_login.png")

        # act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class ='content-header']/h1").text
        # exp_dashboard_text = "Dashboard"

        # if act_dashboard_text == exp_dashboard_text:
        #
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot("..\\screenshots\\valid_login.png")
        #     self.driver.close()
        #     assert False

    # def test_invalid_admin_login(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.admin_page_url)
    #
    #     self.admin_lp = Login_Admin_Page(self.driver)
    #     self.admin_lp.enter_username(self.username)
    #     self.admin_lp.enter_password(self.invalid_password)
        # self.admin_lp.click_login()
        # time.sleep(5)
        #
        # error_message = self.driver.find_element(By.XPATH, "//div[@class "
        #                                                    "='message-error validation-summary-errors']/ul/li").text
        # if error_message == "The credentials provided are incorrect":
        #     assert True
        #     self.driver.close()
        # else:
        #     self.driver.close()
        #     assert False
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_valid_admin_login(self, setup):
        self.logger.info("******** we are in Test 01 admin login class ******")
        self.logger.info("******** verification of login ******")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        # self.admin_lp.enter_username(self.username)
        # self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()


        act_dashboard_text = self.driver.find_element(By.XPATH, "//div[@class ='content-header']/h1").text
        exp_dashboard_text = "Dashboard"

        if act_dashboard_text == exp_dashboard_text:

            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("..\\screenshots\\valid_login.png")
            self.driver.close()
            assert False








