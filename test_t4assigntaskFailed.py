# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestT4assigntaskFailed():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_t4assigntaskFailed(self):
    self.driver.get("http://localhost:3000/")
    self.driver.set_window_size(1103, 637)
    self.driver.find_element(By.CSS_SELECTOR, ".navbar").click()
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "email").send_keys("abhi1801jeet@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("admin")
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("deadloss1801@gmail.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("pass")
    self.driver.find_element(By.CSS_SELECTOR, "button").click()
    self.driver.find_element(By.CSS_SELECTOR, "h1").click()
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    self.driver.find_element(By.LINK_TEXT, "Dashboard").click()
    element = self.driver.find_element(By.LINK_TEXT, "Dashboard")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".tablinks:nth-child(1)").click()
    self.driver.find_element(By.ID, "title").click()
    self.driver.find_element(By.ID, "title").send_keys("task3")
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys("es")
    self.driver.find_element(By.ID, "client").click()
    self.driver.find_element(By.ID, "client").send_keys("deadloss1801@gmail.com")
    self.driver.find_element(By.ID, "assignedTo").click()
    self.driver.find_element(By.ID, "assignedTo").send_keys("202151002@iiitvadodara.ac.in")
    self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(13)").click()
  
