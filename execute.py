import bacon
import time
import re


file_name = 'example.bacon'

def run_parser():
    text = ""
    with open(file_name, 'r') as file:
        text = file.read()

    if text.strip() == "":
        return
    result, error = bacon.run(file_name, text)

    if error:
        print(error.as_string())
    else:
        return result

def parse_input_string(input_string):
    # Remove square brackets from the start and end of the string
    input_string = input_string[1:-1]
    
    # Split the string into tokens
    tokens = re.split(r'(\(|\)|\[|\]|,)', input_string)
    
    # Remove empty strings and whitespace from the list of tokens
    tokens = [token.strip() for token in tokens if token.strip()]
    
    # Initialize stack and result list
    stack = []
    result = []
    
    for token in tokens:
        if token == '[' or token == '(':
            # If the token is an opening bracket, push it onto the stack
            stack.append(token)
        elif token == ']' or token == ')':
            # If the token is a closing bracket, pop items from the stack until we reach the corresponding opening bracket
            temp = []
            while stack and stack[-1] not in ['[', '(']:
                temp.append(stack.pop())
            stack.pop()
            
            # Reverse the order of items in temp and append it to the stack as a tuple
            temp.reverse()
            stack.append(tuple(temp))
        elif token == ',':
            # If the token is a comma, ignore it
            continue
        else:
            # If the token is anything else, push it onto the stack
            stack.append(token)
    
    # Pop remaining items from the stack and append them to the result list
    while stack:
        result.append(stack.pop())
    
    # Reverse the order of items in result and return it as a tuple
    result.reverse()
    return tuple(result)

def convert_to_tuple(input_list):
    result = []
    for item in input_list:
        if isinstance(item, list):
            result.append(convert_to_tuple(item))
        else:
            result.append(item)
    return tuple(result)


start_time = time.time()
# Calculate Run Time
finish_time = time.time()
total_run_time = finish_time - start_time
print("\n", file_name, "runs in:", total_run_time, "seconds")

exp = parse_input_string(str(run_parser()))
tuple_exp = convert_to_tuple(exp)
print(tuple_exp)
