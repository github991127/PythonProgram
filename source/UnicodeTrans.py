from unicodedata import normalize

if __name__ == "__main__":
    with open('test.txt', 'r')as f:
    data = f.read()
    data=normalize('NFKC', data)
    print(data)
