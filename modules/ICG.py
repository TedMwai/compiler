class IntermediateCodeGenerator:
    def __init__(self, ast):
        # Initialize the temporary variable counter and the abstract syntax tree
        self.temp_var_counter = 0
        self.ast = ast

    def get_next_temporary_variable(self):
        # Increment the temporary variable counter and return the previous value
        self.temp_var_counter += 1
        return self.temp_var_counter - 1

    def get_current_temporary_variable(self):
        # Return the current value of the temporary variable counter
        return self.temp_var_counter - 1

    def generate_intermediate_code(self):
        # If the abstract syntax tree is None, return an empty string
        if self.ast == None:
            return ''
        # Otherwise, generate intermediate code using the abstract syntax tree
        return self.ast.get_ic(self.get_next_temporary_variable, self.get_current_temporary_variable)