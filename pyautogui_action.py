import pyautogui
import re
import pygetwindow



'''
  This point is origin
       ↓
      → ←----------------------------
       ↑                            | 
       |                            |
       |                            |
       |                            |
       |      THIS IS WINDOW        | Application window
       |                            |
       |                            |
       |                            |
       |                            |
       -----------------------------
'''



'''
Function: actionOnImage
Input:
 + iconName: which wanted image needs to find on screen
 + delayTime: delay time for action
 + action: Can be 'CLICK', 'MOVE_ONLY' | default is 'CLICK'
 + mousePosition: Can be 'CENTER', 'ORIGIN', 'BOTTOM_LEFT_END', 'BOTTOM_RIGHT_END' | default is 'CENTER'
Output:
 + If there is no icon on screen -> return None
 + Action if valid icon
'''

#TODO: implement BOTTOM_LEFT_END, BOTTOM_RIGHT_END
def actionOnImage(iconName: str, delayTime=None, action='CLICK', mousePosition='CENTER'):
    if (imageLocation := pyautogui.locateOnScreen(iconName)) != None:
        x_imageLocation = imageLocation[0]
        y_imageLocation = imageLocation[1]
        width_imageLocation = imageLocation[2]
        height_imageLocation = imageLocation[3]
        if action == 'CLICK' and mousePosition == 'CENTER':
            pyautogui.click(x_imageLocation + width_imageLocation/2,
                            y_imageLocation + height_imageLocation/2)
        elif action == 'MOVE_ONLY' and mousePosition == 'CENTER':
            pyautogui.moveTo(x_imageLocation + width_imageLocation/2,
                             y_imageLocation + height_imageLocation/2)
        elif action == 'CLICK' and mousePosition == 'ORIGIN':
            pyautogui.click(x_imageLocation, y_imageLocation)
        elif action == 'MOVE_ONLY' and mousePosition == 'ORIGIN':
            pyautogui.click(x_imageLocation, y_imageLocation)
        else:
          raise Exception("Not a valid argument")

    else:
        raise Exception("Can not find input image?")

def getActiveWindow(title:str):
  pass

'''
Function: focusOnWindowWithTitle
Input:
 + title: Name of window, just program name is OK
Output:
 + -1: There is no title like input
 + 0: Focus successfully 
'''

def focusOnWindowWithTitle (title : str):

  for _, item in enumerate(pygetwindow.getAllTitles()):
    if title in item:
      print('Focus on: ' + str(item))
      window = pygetwindow.getWindowsWithTitle(str(item))
      window[0].activate()
      return 0
  return -1


'''
Function takeScreenShot
Input:
 + File name: screenshot file name.
 + Extension: png (can not change this)
Output
'''
def takeScreenShot(fileName:str, extension='.png'):
  pyautogui.screenshot(fileName + extension)
