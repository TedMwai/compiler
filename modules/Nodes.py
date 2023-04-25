from modules.Lexer import Token
from modules.Token import *

# NODES
class NumberNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class StringNode:
    def __init__(self, tok):
        self.tok = tok
        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'


class ListNode:
    def __init__(self, element_nodes, pos_start, pos_end):
        self.element_nodes = element_nodes
        self.pos_start = pos_start
        self.pos_end = pos_end

    def __repr__(self):
        return f'{self.element_nodes}'


class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end

    def __repr__(self):
        return f'{self.var_name_tok}'


class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node
        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end

    def __repr__(self):
        return f'{self.var_name_tok}, {self.value_node}'


class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'


class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'


class IfNode:
    def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (
            self.else_case or self.cases[len(self.cases) - 1])[0].pos_end

        # Token definition for the representation function
        self.if_token = Token(TT_KEYWORD, 'IF')
        self.else_token = Token(TT_KEYWORD, 'ELSE')
        self.then_token = Token(TT_KEYWORD, 'THEN')
        self.elif_token = Token(TT_KEYWORD, 'ELIF')

    def __repr__(self):
        if self.else_case is not None:
            # Start with the IF keyword and its condition
            res = f"{self.if_token}, {self.cases[0][0]}"

            # Add the THEN keyword and its statement
            res += f", {self.then_token}, {self.cases[0][1]}"

            # Add all the ELIF keywords, their conditions, and their statements
            for case in self.cases[1:]:
                res += f", {self.elif_token}, {case[0]}"
                res += f", {self.then_token}, {case[1]}"

            # Add the ELSE keyword and its statement
            res += f"{self.else_token}, {self.else_case}"
            
        else:
            # Start with the IF keyword and its condition
            res = f"{self.if_token}, {self.cases[0][0]}"

            # Add the THEN keyword and its statement
            res += f", {self.then_token}, {self.cases[0][1]}"

            # Add all the ELIF keywords and their conditions
            for case in self.cases[1:]:
                res += f", {self.elif_token}, {case[0]}"
                res += f", {self.then_token}, {case[1]}"
            
            # Add the ELSE keyword and its statement
            res += f"{self.else_token}, {self.else_case}"
        return res


class ForNode:
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node, should_return_null):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end

        # Token definition for the representation function
        self.for_token = Token(TT_KEYWORD, 'FOR')
        self.to_token = Token(TT_KEYWORD, 'TO')
        self.then_token = Token(TT_KEYWORD, 'THEN')
        self.step_token = Token(TT_KEYWORD, 'STEP')

    def __repr__(self):
        res = f"{self.for_token}, {self.var_name_tok}, {self.to_token}, {self.end_value_node}, {self.step_token}, {self.step_value_node}, {self.then_token}, {self.body_node}"
        return res


class WhileNode:
    def __init__(self, condition_node, body_node, should_return_null):
        self.condition_node = condition_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end

        # Token defintion for the representation function
        self.while_token = Token(TT_KEYWORD, 'WHILE')
        self.then_token = Token(TT_KEYWORD, 'THEN')

    def __repr__(self):
        res = f"{self.while_token}, {self.condition_node}, {self.then_token}, {self.body_node}"
        return res


class FuncDefNode:
    def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node
        self.should_auto_return = should_auto_return

        if self.var_name_tok:
            self.pos_start = self.var_name_tok.pos_start
        elif len(self.arg_name_toks) > 0:
            self.pos_start = self.arg_name_toks[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end

        # Token definition for the representation function
        self.fun_token = Token(TT_KEYWORD, 'FUN')

    def __repr__(self):
        return f"{self.fun_token}, {self.var_name_tok}, {self.arg_name_toks}, {self.body_node}"


class CallNode:
    def __init__(self, node_to_call, arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes

        self.pos_start = self.node_to_call.pos_start

        if len(self.arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end

        # Token definition for the representation function
        self.open_paren_token = Token(TT_LPAREN, '(')
        self.close_paren_token = Token(TT_RPAREN, ')')
        self.comma_token = Token(TT_COMMA, ',')
        # self.dot_token = Token(TT_DOT, '.')
        self.arrow_token = Token(TT_ARROW, '->')

    def __repr__(self):
        return f"{self.node_to_call}, {self.open_paren_token}, {self.arg_nodes}, {self.close_paren_token}"


class ReturnNode:
    def __init__(self, node_to_return, pos_start, pos_end):
        self.node_to_return = node_to_return

        self.pos_start = pos_start
        self.pos_end = pos_end

        # Token definition for the representation function
        self.return_token = Token(TT_KEYWORD, 'RETURN')

    def __repr__(self):
        return f"{self.return_token}, {self.node_to_return}"


class ContinueNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end

        # Token definition for the representation function
        self.continue_token = Token(TT_KEYWORD, 'CONTINUE')

    def __repr__(self):
        return f"{self.continue_token}"


class BreakNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end

        # Token definition for the representation function
        self.break_token = Token(TT_KEYWORD, 'BREAK')

    def __repr__(self):
        return f"{self.break_token}"
