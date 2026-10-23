import time
from pynput.mouse import Button, Controller as MouseController
from src.shared.typings import XYCoordinate

_mouse = MouseController()


def drag(x1y1: XYCoordinate, x2y2: XYCoordinate):
    """Arrasta do ponto x1y1 para x2y2 com micro-delays para que o jogo/X11 registre o movimento."""
    _mouse.position = (int(x1y1[0]), int(x1y1[1]))
    time.sleep(0.02)
    _mouse.press(Button.left)
    time.sleep(0.02)
    _mouse.position = (int(x2y2[0]), int(x2y2[1]))
    time.sleep(0.02)
    _mouse.release(Button.left)


def leftClick(windowCoordinate: XYCoordinate = None):
    """Clique com o botão esquerdo, opcionalmente movendo antes para a coordenada."""
    if windowCoordinate is not None:
        _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))
        time.sleep(0.01)
    _mouse.press(Button.left)
    time.sleep(0.01)
    _mouse.release(Button.left)


def moveTo(windowCoordinate: XYCoordinate):
    _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))


def rightClick(windowCoordinate: XYCoordinate = None):
    """Clique com o botão direito, opcionalmente movendo antes para a coordenada."""
    if windowCoordinate is not None:
        _mouse.position = (int(windowCoordinate[0]), int(windowCoordinate[1]))
        time.sleep(0.01)
    _mouse.press(Button.right)
    time.sleep(0.01)
    _mouse.release(Button.right)


def scroll(clicks: int):
    _mouse.scroll(0, clicks)
