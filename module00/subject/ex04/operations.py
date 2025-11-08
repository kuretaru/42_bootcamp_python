import sys
import math


def calc(a, b):
    print(f"Sum:\t\t{a+b}")
    print(f"Difference:\t{a-b}")
    print(f"Product:\t{a*b}")
    if (b == 0):
        print("Quotient:\tERROR (division by zero)")
        print("Quotient:\tERROR (division by zero)")
    else:
        print(f"Quotient:\t{a/b}")
        print(f"Remainder:\t{a%b}")


if __name__ == "__main__":
    match len(sys.argv):
        case 3:
            try:
                calc(int(sys.argv[1]), int(sys.argv[2]))
            except ValueError:
                print("AssertionError: only integers")
        case 2:
            print("AssertionError:  two arguments are required")
        case 1:
            print("Usage: python operations.py <number1> <number2>")
            print("Example:")
            print("\tpython operations.py 10 3")
        case default:
            print("AssertionError: too many arguments")
