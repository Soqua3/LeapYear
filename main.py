def is_year_leap():
    a = int(input("insert year: "))

    if a % 4 == 0:
        print("leap year")
    else:
        print("not a leap year")


if __name__ == "__main__":
    is_year_leap()
