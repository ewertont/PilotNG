from src.utils.mouse import drag, leftClick, moveTo, rightClick, scroll
from pynput.mouse import Button


def test_should_drag(mocker):
    x0y0WindowCoordinate = (0, 0)
    x1y1WindowCoordinate = (1, 1)
    press_spy = mocker.patch('src.utils.mouse._mouse.press')
    release_spy = mocker.patch('src.utils.mouse._mouse.release')
    drag(x0y0WindowCoordinate, x1y1WindowCoordinate)
    press_spy.assert_called_once_with(Button.left)
    release_spy.assert_called_once_with(Button.left)


def test_should_call_leftClick_without_params_when_windowCoordinate_is_None(mocker):
    press_spy = mocker.patch('src.utils.mouse._mouse.press')
    release_spy = mocker.patch('src.utils.mouse._mouse.release')
    leftClick()
    press_spy.assert_called_once_with(Button.left)
    release_spy.assert_called_once_with(Button.left)


def test_should_call_leftClick_with_params_when_windowCoordinate_is_not_None(mocker):
    windowCoordinate = (10, 20)
    press_spy = mocker.patch('src.utils.mouse._mouse.press')
    release_spy = mocker.patch('src.utils.mouse._mouse.release')
    leftClick(windowCoordinate)
    press_spy.assert_called_once_with(Button.left)
    release_spy.assert_called_once_with(Button.left)


def test_should_call_moveTo_with_correct_params(mocker):
    windowCoordinate = (10, 20)
    moveTo(windowCoordinate)


def test_should_call_scroll_with_correct_params(mocker):
    scrolls = 5
    scroll_spy = mocker.patch('src.utils.mouse._mouse.scroll')
    scroll(scrolls)
    scroll_spy.assert_called_once_with(0, 5)


def test_should_call_rightClick_without_params_when_windowCoordinate_is_None(mocker):
    press_spy = mocker.patch('src.utils.mouse._mouse.press')
    release_spy = mocker.patch('src.utils.mouse._mouse.release')
    rightClick()
    press_spy.assert_called_once_with(Button.right)
    release_spy.assert_called_once_with(Button.right)


def test_should_call_rightClick_with_params_when_windowCoordinate_is_not_None(mocker):
    windowCoordinate = (10, 20)
    press_spy = mocker.patch('src.utils.mouse._mouse.press')
    release_spy = mocker.patch('src.utils.mouse._mouse.release')
    rightClick(windowCoordinate)
    press_spy.assert_called_once_with(Button.right)
    release_spy.assert_called_once_with(Button.right)
