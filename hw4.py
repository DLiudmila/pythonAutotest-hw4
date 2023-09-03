from testpage import OperationsHelper
import time
import yaml
import requests
import logging


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_web1(browser):
    logging.info('Test1 Starting')
    testpage = OperationsHelper(browser)
    testpage.open_site()
    testpage.send_login('hacker')
    testpage.send_password(testdata['password'])
    testpage.subbmit_login()
    assert testpage.get_error_message() == '401'


def test_web2(browser):
    testpage = OperationsHelper(browser)
    testpage.open_site()
    testpage.send_login(f"{testdata['username']}")
    testpage.send_password(f"{testdata['password']}")
    testpage.subbmit_login()
    testpage.click_contact_button()
    testpage.enter_name(f"{testdata['name']}")
    testpage.enter_email(f"{testdata['email']}")
    testpage.enter_content(f"{testdata['content1']}")
    time.sleep(testdata['sleep_time'])
    testpage.click_contact_us_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_alert_text() == 'Form successfully submitted'


def test_api1(login):
    obj_data = requests.post(url=testdata['url2'], data={'username': testdata['username'], 'password': testdata['password']})
    token = obj_data.json()['token']
    post = requests.post(url=testdata['url1'], headers={'X-Auth-Token': token}, params={'title': testdata['title'], 'description': testdata['description'], 'content': testdata['content']})
    my_post = post.json()['description']
    assert testdata['description'] in my_post

