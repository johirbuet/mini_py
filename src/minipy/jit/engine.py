from __future__ import annotations

import ctypes
import sys

from llvmlite import binding as llvm


def create_engine():
    # NOTE:
    # llvmlite.binding.initialize() is deprecated and raises RuntimeError in LLVM 20+.
    # LLVM core initialization is automatic now. Remove initialize() calls.  ✅
    # We still must initialize the native target + asmprinter before codegen.
    llvm.initialize_native_target()
    llvm.initialize_native_asmprinter()

    # Helpful early check for OS configs that forbid executable memory
    llvm.check_jit_execution()

    target = llvm.Target.from_default_triple()
    tm = target.create_target_machine(jit=True)

    # Create an empty backing module
    backing_mod = llvm.parse_assembly("")
    engine = llvm.create_mcjit_compiler(backing_mod, tm)
    return engine


def compile_ir(engine, llvm_ir: str):
    mod = llvm.parse_assembly(llvm_ir)
    mod.verify()
    engine.add_module(mod)
    engine.finalize_object()

    # macOS + LLVM 20 known issue: run_static_constructors may assert/segfault.
    # So we skip it on darwin (and you likely don't need it for this MVP anyway).
    if sys.platform != "darwin":
        try:
            engine.run_static_constructors()
        except Exception:
            # Safe to ignore for this toy language unless you rely on globals w/ ctors.
            pass

    return mod


def get_callable(engine, fn_name: str):
    addr = engine.get_function_address(fn_name)
    return ctypes.CFUNCTYPE(ctypes.c_double)(addr)