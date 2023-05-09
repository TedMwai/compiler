import bacon

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
        print("\n\t\t--------------------INTERMEDIATE CODE--------------------\n")
        print(result)


run_parser()