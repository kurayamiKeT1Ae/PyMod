


class PyModError(Exception):
    """
    TODO: main pymoderror class
    """
    pass

class LoadPyModPKGError(PyModError):
    """
    TODO: load pymodpkg json file error
    """
    pass

class RunCommandNotFound(PyModError):
    """
    TODO: run command not found in the pymodPKG.json file
    """
    pass


class PY_SYNTAX_ERROR(PyModError):
    """
    TODO: python syntax's error
    """
    pass