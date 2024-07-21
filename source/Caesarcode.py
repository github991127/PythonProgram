import os
path='./Caesarcode'
def Caesarcode (cleartext):
    order = 0
    i = 1
    list=[]
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
    #print (count)
    while i<count:
        str = ''
        j = 0
        while j<=len(cleartext)-1:
            if (cleartext[j] >= 'a' and cleartext[j] <= 'z'):order = 97#a-z:97-122
            if (cleartext[j] >= 'A' and cleartext[j] <= 'Z'):order = 65#A-Z:65-90
            if (cleartext[j] >= '0' and cleartext[j] <= '9'): order = 48#0-9:48-57
            if order in [65,97]:
                letter=ord(cleartext[j])-order#ord()字符转换为ASCII码
                letter=(letter+i)%26
                str=str+chr(order+letter)#chr()ASCII码转换为字符
            elif order==48:
                letter = ord(cleartext[j]) - order
                letter = (letter + i) % 10
                str = str + chr(order + letter)
            else:
                str = str+cleartext[j]
            j += 1
            order = 0
        i += 1
        list.append(str)
    return list
def file(cleartext,ciphertext,name):
    if not os.path.exists(path):#如果文件夹不存在就创建
        os.mkdir(path)
    fo = open(path+'/'+name, "w")
    fo.write("明文:\n")
    fo.write(cleartext + "\n")

    fo.write("密文:\n")
    print("密文:")
    for x in ciphertext:
        fo.write(x)
        fo.write("\n")
        print(x)
    fo.close()
def main():
    name = "Caesarcode.txt"
    #cleartext='1Q2W3E'
    cleartext=str(input("明文:\n"))#str()数字转换为字符数字
    ciphertext = Caesarcode (cleartext)
    file(cleartext,ciphertext,name)
if __name__ == "__main__":
    main()