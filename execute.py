import bacon
import time

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
        print(result)


start_time = time.time()
run_parser()

# Calculate Run Time
finish_time = time.time()
total_run_time = finish_time - start_time
print("\n", file_name, "runs in:", total_run_time, "seconds")