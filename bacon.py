from modules.Lexer import Lexer
from modules.Parser import Parser
from modules.ICG import IntermediateCodeGenerator

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error
    print("\n\t\t--------------------TOKENS--------------------\n")
    print(tokens)
    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error:
        return None, ast.error
    print("\n\t\t--------------------AST--------------------\n")
    print(ast.node)

    icg = IntermediateCodeGenerator(ast.node)
    return icg.generate_intermediate_code(), ast.error
