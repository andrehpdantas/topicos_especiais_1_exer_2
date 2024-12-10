# This sample code supports Appium Python client >=2.3.0
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

import time
from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def get_sec(time_str):
        """Get seconds from time."""
        m, s = time_str.split(':')
        return int(m) * 60 + int(s)

class PomodoroTimer:
    def __init__(self, driver):
        self.driver = driver
  
    def configure_time(self, m):
    
        el1 = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/clock_settings")
        el1.click()

        pomodoro_duration_input_val = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.pomodrone.app:id/number_input_value\"]")
        pomodoro_duration_value = int(pomodoro_duration_input_val.text)

        el2 = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/settings_pomodoro_duration")
        el2.click()

        eplus = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_plus")
        eminus = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_minus")

        while pomodoro_duration_value != m:
            if m > pomodoro_duration_value:
                eplus.click()
            elif m < pomodoro_duration_value:
                eminus.click()
            
            pomodoro_duration_input_val = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_value")
            pomodoro_duration_value = int(pomodoro_duration_input_val.text)
        
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_close")
        el6.click()

        settings_pomodoro_duration_input_val = self.driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.pomodrone.app:id/number_input_value\"]")
        configured_time = settings_pomodoro_duration_input_val.text

        el7 = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/settings_back")
        el7.click()

        time.sleep(2)

        return configured_time

    def start_stop_timer(self):
        start_stop_btn = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/clockView")
        start_stop_btn.click()

        time.sleep(2)

    def get_time_left(self):
        etimeLeft = self.driver.find_element(by=AppiumBy.ID, value = "com.pomodrone.app:id/clock_timeLeft")
        return get_sec(etimeLeft.text)
    
    
    def get_clock_active_state(self):
        active_state = self.driver.find_element(by=AppiumBy.ID, value = "com.pomodrone.app:id/clock_activeState")
        return active_state.text

    def reset(self):
        reset_btn = self.driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/reset_button")
        reset_btn.click()

