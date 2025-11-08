import sys


def main():
    """
    Offers an updated list of the string and after which filters it with selected rules.

    Returns:
        None: If some Error accured.
    """
    punctuation = [
        "\"", "'", ":", ":", "/", "?", "\\", ".", ">", ",", "<", "[", "{", "]",
        "}", "|", "-", "_", "!", "`", "~", "(", ")"
    ]
    try:
        N = int(sys.argv[2])
    except ValueError:
        print("ERROR!")
        return
    if len(sys.argv) == 3:
        S = sys.argv[1]
        N = sys.argv[2]
        S_upd = ""
        item = 0
        for symbol in S:
            if symbol not in punctuation:
                S_upd += symbol
        S_splited = S_upd.split(" ")
        new_S = []
        for i in range(len(S_splited)):
            if len(S_splited[i]) > int(N):
                new_S.append(S_splited[i])
        print(new_S)
    else:
        print("ERROR!")


if __name__ == "__main__":
    main()
