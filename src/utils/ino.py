# Arduino não é utilizado no modo software (Linux).
# Este módulo é mantido como stub para compatibilidade com código que eventualmente
# chame sendCommandArduino. Os comandos são simplesmente ignorados.

def sendCommandArduino(command):
    """No-op: Arduino desabilitado, inputs simulados via pynput."""
    pass