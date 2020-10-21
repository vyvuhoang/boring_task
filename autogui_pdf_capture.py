import pyautogui
import re
from pyautogui_action import *
import time

'''
Example: Capture PDF Adobe reader page by page
+ Open Adobe by hand
+ This tool will auto set fit one page mode and 
  press button down until end of the file.
'''

focusOnWindowWithTitle('Adobe')
'''
  Get location of window
  This point is origin
       ↓
      → ←----------------------------
       ↑                            |
       |      THIS IS WINDOW        |
       |                            |
       |                            |
       |                            |
       |                            |
       -----------------------------
'''

actionOnImage('./icon/icon_bottom_menu.PNG')
time.sleep(1)
actionOnImage('./icon/hand_bottom.PNG')
actionOnImage('./icon/hand_fit_one_page.PNG')
actionOnImage('./icon/hide_bottom_menu.PNG')
#TODO: Implement screenshot 
while (pyautogui.locateOnScreen("./icon/Capture.PNG") == None):
  pyautogui.press('down')
  time.sleep(0.2)
