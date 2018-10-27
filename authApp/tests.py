import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/gecko')
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/chrome')
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR,'/edge')

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AccountTestCase(LiveServerTestCase):

    def test_login(self):

        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1:8000/accounts/login/')

        username = driver.find_element_by_id('id_username')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_tag_name('button')

        username.send_keys('username')
        password.send_keys('password')
        submit.send_keys(Keys.RETURN)


    def test_login2(self):

        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/accounts/login/')

        username = driver.find_element_by_id('id_username')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_tag_name('button')

        username.send_keys('username')
        password.send_keys('password')
        submit.send_keys(Keys.RETURN)


    def test_login3(self):

        driver = webdriver.Edge()
        driver.get('http://127.0.0.1:8000/accounts/login/')

        username = driver.find_element_by_id('id_username')
        password = driver.find_element_by_id('id_password')
        submit = driver.find_element_by_tag_name('button')

        username.send_keys('username')
        password.send_keys('password')
        submit.send_keys(Keys.RETURN)
    


    



        

