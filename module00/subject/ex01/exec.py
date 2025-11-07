import sys

if (len(sys.argv) > 1):
    arguments = sys.argv[1:]
    full_string = ' '.join(arguments)
    reversed_string = full_string[::-1]
    result = reversed_string.swapcase()
    print(result)
