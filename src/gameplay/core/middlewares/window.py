import platform
import re
import subprocess
from ...typings import Context


def _get_tibia_window_linux():
    """Busca a janela do Tibia no X11 via python-xlib e retorna um objeto
    com .left, .top, .width, .height e .activate() para compatibilidade."""
    try:
        from Xlib import display as xdisplay

        d = xdisplay.Display()
        root = d.screen().root

        def _get_window_name(win):
            try:
                return win.get_wm_name() or ''
            except Exception:
                return ''

        def _search(win, pattern):
            name = _get_window_name(win)
            if pattern.match(name):
                return win
            try:
                children = win.query_tree().children
            except Exception:
                return None
            for child in children:
                result = _search(child, pattern)
                if result:
                    return result
            return None

        regex = re.compile(r'Tibia.*', re.IGNORECASE)
        tibia_win = _search(root, regex)

        if tibia_win is None:
            d.close()
            return None

        geom = tibia_win.get_geometry()
        translated = tibia_win.translate_coords(root, 0, 0)
        win_id = tibia_win.id
        d.close()

        class _WindowInfo:
            def __init__(self, window_id, left, top, width, height):
                self._window_id = window_id
                self.left = left
                self.top = top
                self.width = width
                self.height = height

            def activate(self):
                """Foca a janela no Linux X11 usando xdotool se disponível."""
                try:
                    subprocess.run(
                        ['xdotool', 'windowactivate', str(self._window_id)],
                        check=False,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                except Exception:
                    pass

        return _WindowInfo(
            window_id=win_id,
            left=translated.x,
            top=translated.y,
            width=geom.width,
            height=geom.height,
        )
    except Exception as e:
        print(f'[window] Erro ao buscar janela do Tibia via Xlib: {e}')
        return None


def _get_tibia_window_windows():
    """Busca a janela do Tibia no Windows via win32gui/pygetwindow."""
    try:
        import win32gui
        import pygetwindow as gw

        windowsList = []
        win32gui.EnumWindows(lambda hwnd, param: param.append(hwnd), windowsList)
        windowsNames = list(map(lambda hwnd: win32gui.GetWindowText(hwnd), windowsList))
        regex = re.compile(r'Tibia - .*')
        windowsFilter = list(filter(lambda name: regex.match(name), windowsNames))
        if len(windowsFilter) > 0:
            return gw.getWindowsWithTitle(windowsFilter[0])[0]
    except Exception as e:
        print(f'[window] Erro ao buscar janela do Tibia via win32gui: {e}')
    return None


# TODO: add unit tests
def setTibiaWindowMiddleware(context: Context) -> Context:
    if context['window'] is None:
        system = platform.system()
        if system == 'Linux':
            context['window'] = _get_tibia_window_linux()
        else:
            context['window'] = _get_tibia_window_windows()
    return context
