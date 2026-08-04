from pynput.mouse import Button, Controller as MouseController
from src.shared.typings import XYCoordinate

_mouse = MouseController()


def drag(x1y1: XYCoordinate, x2y2: XYCoordinate):
    _mouse.position = (int(x1y1[0]), int(x1y1[1]))
    _mouse.press(Button.left)
    _mouse.position = (int(x2y2[0]), int(x2y2[1]))
    _mouse.release(Button.left)


def leftClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is not None:
        _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))
    _mouse.press(Button.left)
    _mouse.release(Button.left)


def moveTo(windowCoordinate: XYCoordinate):
    _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))


def rightClick(windowCoordinate: XYCoordinate = None):
    if windowCoordinate is not None:
        _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))
    _mouse.press(Button.right)
    _mouse.release(Button.right)


def scroll(clicks: int):
    _mouse.scroll(0, clicks)
