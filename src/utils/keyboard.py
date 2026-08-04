import keyboard

def getAsciiFromKey(key):
    if not key:
        return None

    sanitized = key.lower()                          

    if sanitized == 'space':
        return ' '
    elif sanitized == 'esc':
        return 'esc'
    elif sanitized == 'ctrl':
        return 'ctrl'
    elif sanitized == 'alt':   
        return 'alt'
    elif sanitized == 'shift':
        return 'shift'
    elif sanitized == 'enter':
        return 'enter'
    elif sanitized == 'up':
        return 'up'
    elif sanitized == 'down':
        return 'down'
    elif sanitized == 'left':
        return 'left'
    elif sanitized == 'right':
        return 'right'
    elif sanitized == 'backspace':
        return 'backspace'
    elif sanitized in [f'f{i}' for i in range(1, 13)]:
        return sanitized
    elif sanitized.isalpha() or sanitized.isdigit():
        return sanitized
    return None

def hotkey(*args):
    keyboard.press_and_release('+'.join(args))

def keyDown(key: str):
    asciiKey = getAsciiFromKey(key)
    if asciiKey:
        keyboard.press(asciiKey)

def keyUp(key: str):
    asciiKey = getAsciiFromKey(key)
    if asciiKey:
        keyboard.release(asciiKey)

def press(*args):
    for key in args:
        asciiKey = getAsciiFromKey(key)
        if asciiKey:
            keyboard.press_and_release(asciiKey)

def write(phrase: str):
    keyboard.write(phrase)
