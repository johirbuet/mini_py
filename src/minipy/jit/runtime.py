"""Optional runtime helpers for builtins.

You can expose host functions to JIT'd code via:
  llvmlite.binding.add_symbol(name, address)
"""

import ctypes

def cfunc_addr(fn) -> int:
    """Return an integer address for a ctypes CFUNCTYPE function."""
    return ctypes.cast(fn, ctypes.c_void_p).value
