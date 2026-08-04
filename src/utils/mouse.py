import pyautogui
from src.shared.typings import XYCoordinate

def drag(x1y1: XYCoordinate, x2y2: XYCoordinate):
    pyautogui.moveTo(int(x1y1[0]), int(x1y1[1]))
    pyautogui.mouseDown()
    pyautogui.moveTo(int(x2y2[0]), int(x2y2[1]))
    pyautogui.mouseUp()

def leftClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.click()
    else:
        pyautogui.click(int(windowCoordinate[0]), int(windowCoordinate[1]))

def moveTo(windowCoordinate: XYCoordinate):
    pyautogui.moveTo(int(windowCoordinate[0]), int(windowCoordinate[1]))

def rightClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is None:
        pyautogui.rightClick()
    else:
        pyautogui.rightClick(int(windowCoordinate[0]), int(windowCoordinate[1]))

def scroll(clicks: int):
    pyautogui.scroll(clicks)
