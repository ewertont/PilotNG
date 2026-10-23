import cv2
from numba import njit
import numpy as np
from PIL import Image
from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import hashit, locate


# TODO: add types
# TODO: add unit tests
def cacheChain(imageList):
    def decorator(_):
        lastX = None
        lastY = None
        lastW = None
        lastH = None
        lastImageHash = None

        def inner(screenshot: GrayImage) -> Union[BBox, None]:
            nonlocal lastX, lastY, lastW, lastH, lastImageHash
            if lastX != None and lastY != None and lastW != None and lastH != None:
                copiedImage = screenshot[lastY:lastY +
                                         lastH, lastX:lastX + lastW]
                copiedImageHash = hashit(copiedImage)
                if copiedImageHash == lastImageHash:
                    return (lastX, lastY, lastW, lastH)
            for image in imageList:
                imagePosition = locate(screenshot, image)
                if imagePosition is not None:
                    (x, y, w, h) = imagePosition
                    lastX = x
                    lastY = y
                    lastW = w
                    lastH = h
                    lastImage = screenshot[lastY:lastY +
                                           lastH, lastX:lastX + lastW]
                    lastImageHash = hashit(lastImage)
                    return (x, y, w, h)
            return None
        return inner
    return decorator


# TODO: add unit tests
@njit(cache=True, fastmath=True)
def convertGraysToBlack(arr: np.ndarray) -> np.ndarray:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i, j] >= 50 and arr[i, j] <= 100:
                arr[i, j] = 0
    return arr


# TODO: add unit tests
def RGBtoGray(image: np.ndarray) -> GrayImage:
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)


# TODO: add unit tests
def loadFromRGBToGray(path: str) -> GrayImage:
    return np.array(RGBtoGray(load(path)), dtype=np.uint8)


# TODO: add unit tests
def save(arr: GrayImage, name: str):
    im = Image.fromarray(arr)
    im.save(name)


# TODO: add unit tests
def crop(image: GrayImage, x: int, y: int, width: int, height: int) -> GrayImage:
    return image[y:y + height, x:x + width]


import os

_dir_cache = {}


def _resolve_case_insensitive_path(path: str) -> str:
    if os.path.exists(path):
        return path
    parent = os.path.dirname(path)
    if not os.path.exists(parent):
        return path
    if parent not in _dir_cache:
        try:
            _dir_cache[parent] = {entry.lower(): entry for entry in os.listdir(parent)}
        except Exception:
            _dir_cache[parent] = {}
    basename = os.path.basename(path).lower()
    actual = _dir_cache[parent].get(basename)
    if actual:
        return os.path.join(parent, actual)
    return path


# TODO: add unit tests
def load(path: str) -> np.ndarray:
    resolved_path = _resolve_case_insensitive_path(path)
    img = cv2.imread(resolved_path)
    if img is None:
        raise FileNotFoundError(f"Image not found at path: {path} (resolved: {resolved_path})")
    return np.array(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), dtype=np.uint8)
