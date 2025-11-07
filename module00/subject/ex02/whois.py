    import sys

if not (len(sys.argv) == 1):
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
    try:
        number = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 1:
        print("I'm Odd.")
    else:
        print("I'm Even.")
