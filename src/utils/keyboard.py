import time
from pynput.keyboard import Key, Controller as KeyboardController

_keyboard = KeyboardController()

# Mapeamento expandido de nomes de tecla para pynput.keyboard.Key
_SPECIAL_KEYS = {
    'space': Key.space,
    'esc': Key.esc,
    'escape': Key.esc,
    'ctrl': Key.ctrl,
    'ctrl_l': Key.ctrl_l,
    'ctrl_r': Key.ctrl_r,
    'alt': Key.alt,
    'alt_l': Key.alt_l,
    'alt_r': Key.alt_r,
    'alt_gr': Key.alt_gr,
    'altgr': Key.alt_gr,
    'shift': Key.shift,
    'shift_l': Key.shift_l,
    'shift_r': Key.shift_r,
    'enter': Key.enter,
    'return': Key.enter,
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right,
    'backspace': Key.backspace,
    'tab': Key.tab,
    'delete': Key.delete,
    'insert': Key.insert,
    'home': Key.home,
    'end': Key.end,
    'page_up': Key.page_up,
    'pageup': Key.page_up,
    'pgup': Key.page_up,
    'page_down': Key.page_down,
    'pagedown': Key.page_down,
    'pgdn': Key.page_down,
    'caps_lock': Key.caps_lock,
    'capslock': Key.caps_lock,
    'num_lock': Key.num_lock,
    'numlock': Key.num_lock,
    'scroll_lock': Key.scroll_lock,
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
    sanitized = key.strip().lower()
    if sanitized in _SPECIAL_KEYS:
        return _SPECIAL_KEYS[sanitized]
    if len(sanitized) == 1:
        return sanitized
    return None


def hotkey(*args):
    """Pressiona e solta uma combinação de teclas (ex: ctrl+c, hotkey('ctrl', 'a'), ou hotkey('ctrl+f1'))."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        raw_keys = args[0]
    elif len(args) == 1 and isinstance(args[0], str) and '+' in args[0]:
        raw_keys = args[0].split('+')
    else:
        raw_keys = args

    # Expande qualquer elemento que contenha '+'
    keys = []
    for k in raw_keys:
        if isinstance(k, str) and '+' in k:
            keys.extend(k.split('+'))
        else:
            keys.append(k)

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
    """Pressiona uma ou mais teclas. Suporta combinações 'ctrl+f1' automaticamente."""
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        keys = args[0]
    else:
        keys = args
    for key in keys:
        if isinstance(key, str) and '+' in key:
            hotkey(key)
            continue
        resolved = _resolveKey(key)
        if resolved:
            _keyboard.press(resolved)
            _keyboard.release(resolved)


def write(phrase: str):
    _keyboard.type(phrase)
