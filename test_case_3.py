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

SLEEP_TIME = 5 

def get_sec(time_str):
    """Get seconds from time."""
    m, s = time_str.split(':')
    return int(m) * 60 + int(s)


def test_case_3():
    SLEEP_TIME = 60

    try:
        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        pomo = PomodoroTimer(driver)
    
        pomo.configure_pomo_time(1)

        time.sleep(1)

        pomo.set_mode("POMODORO")

        pomo.start_stop_timer()
        time_start = pomo.get_time_left()

        i = SLEEP_TIME
        while i != 0:
            print(f'Active State: {pomo.get_clock_active_state()}')
            time.sleep(1)
            i = i -1

        time.sleep(5)
        
        active_state = pomo.get_clock_active_state()
        assert active_state == "SHORT BREAK"

        pomo.start_stop_timer()
        pomo.reset()
     
    finally:
        driver.quit()