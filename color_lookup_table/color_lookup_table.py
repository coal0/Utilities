FG = "\033[38;5;{}m"
BG = "\033[48;5;{}m"
RST = "\033[0m"


def print_256_color_lookup_table_for(x):
    if x == "foreground" or x == "fg":
        x = FG
    elif x == "background" or x == "bg":
        x = BG
    else:
        raise ValueError("Unrecognized value for argument.")

    for n in range(16):
        # Standard and high intensity colors
        print(x.format(n), str(n).rjust(3), RST, end=" ")
    print()

    for n in range(16, 232):
        # 216 colors
        print(x.format(n), str(n).rjust(3), RST, end=" ")
        if (n - 15) % 36 == 0:
            print()

    for n in range(232, 256):
        # Grayscale colors
        print(x.format(n), str(n).rjust(3), RST, end=" ")
    print()


def print_256_color_lookup_table():
    print_256_color_lookup_table_for("foreground")
    print("\n\n")
    print_256_color_lookup_table_for("background")


def main():
    print_256_color_lookup_table()

if __name__ == "__main__":
    main()
