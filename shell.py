import bacon

while True:
    text = input('bacon > ')
    result, error = bacon.run('<stdin>', text)

    if error:
        print(error.as_string())
    elif result:
        print(result)
