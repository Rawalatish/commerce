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
from utilities import excel_util

class Test_02_Admin_Login_data_driven:

    # we defined above in the config so we will call it from there
    # username and password we can access from test data excel sheet

    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_password = Read_Config.get_invalid_password()

    logger = Log_Maker.log_gen()
    path = ".//test_data//admin_login_info.xlsx"            # test data file path

    status_list = []

    def test_valid_admin_login_data_driven(self, setup):

        self.logger.info("************ admin login test via data driven - started **********")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)


        self.rows = excel_util.get_row_count(self.path, "Sheet1")
        print(" no. of rows: ", self.rows)

        for r in range(2 , self.rows+1):
            self.username = excel_util.read_data(self.path, "Sheet1", r, 1)
            self.password = excel_util.read_data(self.path, "Sheet1", r, 2)
            self.exp_login = excel_util.read_data(self.path, "Sheet1", r, 3)
            time.sleep(5)

        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        self.driver.save_screenshot("..\\screenshots\\valid_login.png")

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if self.exp_login == "Yes":
                self.logger.info("**** test data is passed ***")
                self.status_list.append("Pass")

            elif self.exp_login == "No":
                self.logger.info("****** test data is failed")
                self.status_list.append("Fail")

        elif act_title != exp_title:
            if self.exp_login == "Yes":
                self.logger.info(" Test data is failed ")
                self.status_list.append("Fail")

            elif self.exp_login == "No":
                self.logger.info("**** test data is passed ***")
                self.status_list.append("Pass")

        print("Status list is, ", self.status_list)

        if "Fail" in self.status_list:
            self.logger.info(" ********** Test admin data driven test is failed ******")
            assert False
        else:
            self.logger.info(" ********** Test admin data driven test is Passed ******")
            assert True



    def test_invalid_admin_login(self, setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)

        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.invalid_password)
        self.admin_lp.click_login()
        time.sleep(5)

        error_message = self.driver.find_element(By.XPATH, "//div[@class "
                                                           "='message-error validation-summary-errors']/ul/li").text
        if error_message == "The credentials provided are incorrect":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False











