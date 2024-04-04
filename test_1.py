import time

import pytest
import yaml

from testpage import OperationsHelper
import logging

with open('testdata.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    name = data['name']
    passwd = data['passwd']


def test_step1(browser):
    logging.info('test_1 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('test_2 Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f'Hello, {name}'


def test_step3(browser):
    logging.info('test_3 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title('testtitle')
    testpage.enter_content('testcontent')
    testpage.enter_description('testdesc')
    testpage.click_save_btn()
    time.sleep(3)
    assert testpage.get_res_text() == 'testtitle'


def test_step4(browser):
    logging.info('test_4 Starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact_link()
    time.sleep(2)
    testpage.enter_contact_name('testname')
    testpage.enter_contact_mail('test@test.ru')
    testpage.enter_contact_content('testcontactcontent')
    testpage.click_contact_us_btn()
    time.sleep(3)
    assert testpage.get_alert_text() == f'Form successfully submitted'


if __name__ == '__main__':
    pytest.main(['-vv'])
