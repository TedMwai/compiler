from modules.Lexer import Lexer
from modules.Parser import Parser


def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    
    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    return ast.node, ast.error

    # Genarate Intermediate Code
    
