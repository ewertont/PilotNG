import os
import platform
import sys

def _ensure_x11_env():
    """
    Garante que as variáveis de ambiente X11 estejam definidas quando rodando como root no Linux.
    Sem DISPLAY e XAUTHORITY, pynput e customtkinter falham silenciosamente.
    """
    if platform.system() != 'Linux':
        return

    if not os.environ.get('DISPLAY'):
        os.environ.setdefault('DISPLAY', ':0')
        print('[main] DISPLAY não definido, usando :0')

    if not os.environ.get('XAUTHORITY'):
        # Localiza o .Xauthority do usuário que iniciou a sessão gráfica
        xauth_candidates = [
            '/root/.Xauthority',
            f"/home/{os.environ.get('SUDO_USER', '')}/.Xauthority",
            '/run/user/1000/gdm/Xauthority',
        ]
        for candidate in xauth_candidates:
            if os.path.exists(candidate):
                os.environ['XAUTHORITY'] = candidate
                print(f'[main] XAUTHORITY definido para: {candidate}')
                break
        else:
            print('[main] AVISO: XAUTHORITY não encontrado. Se a UI ou o input falhar, defina manualmente: export XAUTHORITY=~/.Xauthority')


from src.gameplay.context import context
from src.gameplay.threads.pilotNG import PilotNGThread
from src.gameplay.threads.ui import UIThread
from src.gameplay.threads.alert import AlertThread
from src.ui.context import Context

def main():
    _ensure_x11_env()
    contextInstance = Context(context)
    uiThreadInstance = UIThread(contextInstance)
    uiThreadInstance.start()
    alertThreadInstance = AlertThread(contextInstance)
    alertThreadInstance.start()
    pilotNGThreadInstance = PilotNGThread(contextInstance)
    pilotNGThreadInstance.mainloop()

if __name__ == '__main__':
    main()
