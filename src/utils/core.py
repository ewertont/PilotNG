import cv2
import mss
import mss.tools
from farmhash import FarmHash64
import numpy as np
from typing import Callable, Union
from src.shared.typings import BBox, GrayImage


import threading

_local_sct = threading.local()
latestScreenshot = None


def _get_sct():
    """Garante uma instância de mss por thread no Linux (mss usa threading.local internamente para X11)."""
    if not hasattr(_local_sct, 'instance') or _local_sct.instance is None:
        _local_sct.instance = mss.mss()
    return _local_sct.instance


# TODO: add unit tests
def cacheObjectPosition(func: Callable) -> Callable:
    lastX = None
    lastY = None
    lastW = None
    lastH = None
    lastImgHash = None

    def inner(screenshot):
        nonlocal lastX, lastY, lastW, lastH, lastImgHash
        if lastX != None and lastY != None and lastW != None and lastH != None:
            if hashit(screenshot[lastY:lastY + lastH, lastX:lastX + lastW]) == lastImgHash:
                return (lastX, lastY, lastW, lastH)
        res = func(screenshot)
        if res is None:
            return None
        lastX = res[0]
        lastY = res[1]
        lastW = res[2]
        lastH = res[3]
        lastImgHash = hashit(
            screenshot[lastY:lastY + lastH, lastX:lastX + lastW])
        return res
    return inner


# TODO: add unit tests
def hashit(arr: np.ndarray) -> int:
    return FarmHash64(np.ascontiguousarray(arr))


# TODO: add unit tests
def locate(compareImage: GrayImage, img: GrayImage, confidence: float = 0.85, type = cv2.TM_CCOEFF_NORMED) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImage, img, type)
    res = cv2.minMaxLoc(match)
    if res[1] <= confidence:
        return None
    return res[3][0], res[3][1], len(img[0]), len(img)


# TODO: add unit tests
def locateMultiple(compareImg: GrayImage, img: GrayImage, confidence: float = 0.85) -> Union[BBox, None]:
    match = cv2.matchTemplate(compareImg, img, cv2.TM_CCOEFF_NORMED)
    loc = np.where(match >= confidence)
    resultList = []
    for pt in zip(*loc[::-1]):
        resultList.append((pt[0], pt[1], len(compareImg[0]), len(compareImg)))
    return resultList


# TODO: add unit tests
def getScreenshot() -> GrayImage:
    global latestScreenshot
    try:
        sct = _get_sct()
        monitor = sct.monitors[1]  # monitor principal (índice 1 = primeiro monitor físico)
        frame = sct.grab(monitor)
        if frame is not None:
            img_bgra = np.array(frame)
            latestScreenshot = cv2.cvtColor(img_bgra, cv2.COLOR_BGRA2GRAY)
            return latestScreenshot
    except Exception:
        pass
    try:
        from PIL import ImageGrab
        img = ImageGrab.grab()
        arr = np.array(img)
        latestScreenshot = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        return latestScreenshot
    except Exception:
        return latestScreenshot

