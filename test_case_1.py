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

from pomodoro_timer import PomodoroTimer

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
    try:
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        pomo = PomodoroTimer(driver)

        configured_valued = pomo.configure_time(1)

        pomo_mode = driver.find_element(by=AppiumBy.ID, value="com.pomodrone.app:id/mode_text2")
        mode_text = pomo_mode.text
        mode_text = mode_text.replace("POMODORO", "")
        mode_text = mode_text.replace("MIN", "")
        mode_text = mode_text.replace(" ", "")

        assert configured_valued == mode_text

    finally:
        driver.quit()
