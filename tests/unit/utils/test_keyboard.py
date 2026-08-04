from src.utils.keyboard import hotkey, keyDown, keyUp, press, write
from pynput.keyboard import Key


def test_should_call_hotkey(mocker):
    press_spy = mocker.patch('src.utils.keyboard._keyboard.press')
    release_spy = mocker.patch('src.utils.keyboard._keyboard.release')
    hotkey('ctrl', 'a')
    assert press_spy.call_count == 2
    assert release_spy.call_count == 2


def test_should_call_keyDown(mocker):
    press_spy = mocker.patch('src.utils.keyboard._keyboard.press')
    keyDown('a')
    press_spy.assert_called_once_with('a')


def test_should_call_keyUp(mocker):
    release_spy = mocker.patch('src.utils.keyboard._keyboard.release')
    keyUp('a')
    release_spy.assert_called_once_with('a')


def test_should_call_press(mocker):
    press_spy = mocker.patch('src.utils.keyboard._keyboard.press')
    release_spy = mocker.patch('src.utils.keyboard._keyboard.release')
    press('a')
    press_spy.assert_called_once_with('a')
    release_spy.assert_called_once_with('a')


def test_should_call_write(mocker):
    phrase = 'hello world!'
    type_spy = mocker.patch('src.utils.keyboard._keyboard.type')
    write(phrase)
    type_spy.assert_called_once_with(phrase)
