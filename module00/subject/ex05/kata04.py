kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    if kata[0] < 0 or kata[1] < 0:
        print("AssertionError: Kata must have 2 non-negative first numbers!")
    elif kata[0] > 100 or kata[1] > 100:
        print(
            "AssertionError: Kata must have 2 first numbers with only 2 digits!"
        )
    else:
        print(
            f"module_{kata[0]:02d}, ex_{kata[1]:02d} : {kata[2]:.2f}, {kata[3]:.2e}, {kata[4]:.2e}"
        )
