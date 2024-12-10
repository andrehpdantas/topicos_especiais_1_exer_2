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
	"appium:automationName": "UIAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

def test_case_4():
    SLEEP_TIME = 5

    try:
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        pomo = PomodoroTimer(driver)
    
        pomo.configure_time(1)

        pomo.start_stop_timer()
        time_start = pomo.get_time_left()
        time.sleep(SLEEP_TIME)
        time_end = pomo.get_time_left()
        pomo.start_stop_timer()
        assert time_start - time_end  >= SLEEP_TIME

        pomo.reset()

    finally:
        driver.quit()
