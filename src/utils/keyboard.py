from pynput.keyboard import Key, Controller as KeyboardController

_keyboard = KeyboardController()

# Mapeamento de nomes de tecla para pynput.keyboard.Key
_SPECIAL_KEYS = {
    'space': Key.space,
    'esc': Key.esc,
    'ctrl': Key.ctrl,
    'alt': Key.alt,
    'shift': Key.shift,
    'enter': Key.enter,
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right,
    'backspace': Key.backspace,
    'tab': Key.tab,
    'delete': Key.delete,
    'f1': Key.f1,
    'f2': Key.f2,
    'f3': Key.f3,
    'f4': Key.f4,
    'f5': Key.f5,
    'f6': Key.f6,
    'f7': Key.f7,
    'f8': Key.f8,
    'f9': Key.f9,
    'f10': Key.f10,
    'f11': Key.f11,
    'f12': Key.f12,
}


def _resolveKey(key: str):
    """Resolve uma string de tecla para o tipo correto do pynput."""
    if not key or not isinstance(key, str):
        return None
    sanitized = key.lower()
    if sanitized in _SPECIAL_KEYS:
        return _SPECIAL_KEYS[sanitized]
    if len(key) == 1:
        return key
    return None


def hotkey(*args):
    """Pressiona e solta uma combinação de teclas (ex: ctrl+c ou hotkey('ctrl', 'a'))."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        keys = args[0]
    else:
        keys = args
    resolved = [_resolveKey(k) for k in keys]
    resolved = [k for k in resolved if k is not None]
    if not resolved:
        return
    modifiers = resolved[:-1]
    main_key = resolved[-1]
    for mod in modifiers:
        _keyboard.press(mod)
    _keyboard.press(main_key)
    _keyboard.release(main_key)
    for mod in reversed(modifiers):
        _keyboard.release(mod)


def keyDown(key: str):
    resolved = _resolveKey(key)
    if resolved:
        _keyboard.press(resolved)


def keyUp(key: str):
    resolved = _resolveKey(key)
    if resolved:
        _keyboard.release(resolved)


def press(*args):
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        keys = args[0]
    else:
        keys = args
    for key in keys:
        resolved = _resolveKey(key)
        if resolved:
            _keyboard.press(resolved)
            _keyboard.release(resolved)


def write(phrase: str):
    _keyboard.type(phrase)
