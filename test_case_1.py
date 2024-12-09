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

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "uiautomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

def test_case_1():
    '''
    CT01 Teste Capacidade de alteração de minutos
    '''
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    el2 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/clock_settings")
    el2.click()

    time.sleep(1)

    el3 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/settings_pomodoro_duration")
    el3.click()
    el4 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_plus")
    el4.click()
    el5 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/switcher_close")
    el5.click()

   
    tSettings_pomodoro_duration_input_val = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@resource-id=\"com.pomodrone.app:id/number_input_value\"]")
    pomodoro_duration_value = tSettings_pomodoro_duration_input_val.text

    driver.execute_script('mobile: pressKey', {"keycode": 4})
    el6 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/clockView")
    el6.click()
    time.sleep(5)
    el6.click()
    time.sleep(5)

    el10 = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/reset_button")
    el10.click()

    time.sleep(1)
  
    tPomodoro = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/mode_text2")
    pomodoro_text = tPomodoro.text
    pomodoro_text = pomodoro_text.replace("POMODORO", "")
    pomodoro_text = pomodoro_text.replace("MIN", "")
    pomodoro_text = pomodoro_text.replace(" ", "")


    assert pomodoro_duration_value == pomodoro_text


    driver.quit()