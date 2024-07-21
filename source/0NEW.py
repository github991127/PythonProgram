def Caesarcode(cleartext):
    order = 0
    i = 1
    list = []
    bool1 = bool2 = 0
    for x in cleartext:
        if x.isdigit():
            count = 10
            bool1 = 1
        if x.isalpha():
            count = 26
            bool2 = 1
    if bool1 and bool2:
        count = 130
    return count


def main():
    # cleartext = str(input("明文:\n"))  # str()数字转换为字符数字
    cleartext = "A1"
    ciphertext = Caesarcode(cleartext)
    print(ciphertext)


if __name__ == "__main__":
    main()
