while True:
    try:
        string = input()
        if not string:
            break
        print(string)
    except EOFError:
        break