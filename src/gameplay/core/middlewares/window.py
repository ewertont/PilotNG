import platform
import re
import subprocess
from ...typings import Context


def _get_tibia_window_linux(window_title: str = None):
    """Busca a janela do Tibia no X11 via python-xlib e retorna um objeto
    com .left, .top, .width, .height, .title e .activate() para compatibilidade."""
    try:
        from Xlib import display as xdisplay, X

        d = xdisplay.Display()
        root = d.screen().root

        def _is_valid_tibia_window(win):
            try:
                name = win.get_wm_name() or ''
                if window_title:
                    if name != window_title and window_title.lower() not in name.lower():
                        return False
                else:
                    if not re.search(r'Tibia', name, re.IGNORECASE):
                        return False
                # Ignora gerenciadores de arquivos, editores, terminais que tenham "Tibia" no título
                wm_class = win.get_wm_class()
                if wm_class and any(c.lower() in ('thunar', 'mousepad', 'xfce4-terminal', 'code', 'terminal') for c in wm_class):
                    return False
                geom = win.get_geometry()
                if geom.width < 300 or geom.height < 300:
                    return False
                attrs = win.get_attributes()
                if attrs and attrs.map_state != X.IsViewable:
                    return False
                return True
            except Exception:
                return False

        def _search(win):
            if _is_valid_tibia_window(win):
                return win
            try:
                children = win.query_tree().children
            except Exception:
                return None
            for child in children:
                result = _search(child)
                if result:
                    return result
            return None

        tibia_win = _search(root)

        if tibia_win is None:
            d.close()
            return None

        geom = tibia_win.get_geometry()
        # root.translate_coords(tibia_win, 0, 0) dá a posição (left, top) de tibia_win em relação ao root
        translated = root.translate_coords(tibia_win, 0, 0)
        win_id = tibia_win.id
        title = tibia_win.get_wm_name() or ''
        d.close()

        class _WindowInfo:
            def __init__(self, window_id, left, top, width, height, title=''):
                self._window_id = window_id
                self.left = left
                self.top = top
                self.width = width
                self.height = height
                self.title = title

            def __repr__(self):
                return f"<Window '{self.title}' id={hex(self._window_id)} pos=({self.left}, {self.top}) size={self.width}x{self.height}>"

            def activate(self):
                """Foca a janela no Linux X11 nativamente via EWMH com fallback para xdotool."""
                try:
                    from Xlib import display as xdisplay_inner, X as X_inner
                    d_inner = xdisplay_inner.Display()
                    root_inner = d_inner.screen().root
                    win_inner = d_inner.create_resource_object('window', self._window_id)

                    net_active = d_inner.intern_atom('_NET_ACTIVE_WINDOW')
                    event = xdisplay_inner.event.ClientMessage(
                        window=win_inner,
                        client_type=net_active,
                        data=(32, [1, X_inner.CurrentTime, 0, 0, 0])
                    )
                    root_inner.send_event(event, event_mask=X_inner.SubstructureRedirectMask | X_inner.SubstructureNotifyMask)
                    try:
                        win_inner.set_input_focus(X_inner.RevertToParent, X_inner.CurrentTime)
                        win_inner.configure(stack_mode=X_inner.Above)
                    except Exception:
                        pass
                    d_inner.sync()
                    d_inner.close()
                except Exception:
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
            title=title,
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
