class MiniPyError(Exception):
    """Base exception for the MiniPy language."""

class ParseError(MiniPyError):
    pass

class CodegenError(MiniPyError):
    pass
