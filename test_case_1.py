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

        configured_valued = pomo.configure_pomo_time(1)

        pomo.set_mode("POMODORO")
        mode_time = pomo.get_time_mode("POMODORO")

        assert configured_valued == mode_time

    finally:
        driver.quit()
