import os

path = './FilesMerging'


def fun1():  # 文件目录下所有文件写入列表
    files = os.listdir('./')
    str_list = []
    for i in files:
        # if ('-' in i): continue  # 若文件名包含-字符，忽视该文件
        file_path = path + '/' + i
        file_name = i.replace('.txt', '')
        str_list.append(file_name)
    return str_list


def fun2(name, str_list):  # 列表写入新文件
    fo = open(path + '/' + name, "w", encoding='utf-8')
    for i in str_list:
        fo.write(i + '\n')
    fo.close()


def FilesMerging():
    name = "FilesMerging.txt"
    if not os.path.exists(path):  # 如果文件夹不存在就创建
        os.mkdir(path)
    str_list = fun1()
    fun2(name, str_list)


if __name__ == '__main__':
    FilesMerging()
