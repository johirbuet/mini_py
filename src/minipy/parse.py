from antlr4 import InputStream, CommonTokenStream

from gen.MiniPyLexer import MiniPyLexer
from gen.MiniPyParser import MiniPyParser


def parse_repl(source: str):
    """Parse a chunk of text using the `repl` start rule."""
    stream = InputStream(source)
    lexer = MiniPyLexer(stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniPyParser(tokens)
    return parser.repl()


def parse_line(line: str):
    """Convenience: parse one REPL line (adds a newline)."""
    return parse_repl(line + "")
