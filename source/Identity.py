def getPowerCode():  # 计算权重系数
    power = []
    for i in range(18):
        power.append(2 ** (i) % 11)  # 从右到左的系数。从左到右的系数为79058 42163 79058 421(0指10)
    return power


def getCheckCode(code, lose):  # 计算权重和

    s = 0
    power = getPowerCode()
    for i in range(18):
        if 18 - lose == i:
            continue
        if code[17 - i] == 'X' or code[17 - i] == 'x':
            s += 10 * power[i]
        else:
            s += int(code[17 - i]) * power[i]

    return s


def identityCheck(code, lose=18):  # 判断合法性+计算校验码
    # 判断输入位数合法性
    length = len(code)
    if length == 18:
        code18 = code
        lose = 0  # 取消lose判断
    elif length == 17:
        code18 = (code[0:lose - 1] + "a" + code[lose - 1:length])  # 缺位暂用a替代
    else:
        return ("FA")  # 输入位数不为17或18
    # 判断缺少位数合法性
    if lose not in range(0, 19):
        return ("FB")  # 缺少位数不在1-18内

    # 使用18位code计算
    s = getCheckCode(code18, lose)
    if length == 18:
        return s % 11 == 1
    else:
        checkNum = []
        for num in range(11):
            power = getPowerCode()

            if (s + num * power[18 - lose]) % 11 == 1:
                if num == 10:
                    checkCode = 'X'
                else:
                    checkCode = str(num)
                checkNum.append(checkCode)
        print(checkNum)
        return code18.replace('a', checkNum[0])


def main():
    lose = 18
    # code = '220202202002020022'  # 身份证True
    code = '22020220200202002'  # 缺少的第18位为2

    # code = '220' # 输入位数不为17或18
    # lose = 19 # 缺少位数不在1-18内
    # code = '2202022020020200x'  # 缺少的第17位为9
    # code = '2202022020020200X'  # 缺少的第17位为9
    # lose = 17

    identity = identityCheck(code, lose)
    if identity == "FA":
        print("输入位数不为17或18")
        exit()
    elif identity == "FB":
        print("缺少位数不在1-18内")
        exit()

    print('身份证{0}'.format(identity))
    if type(identity) != bool:
        print('缺少的第{0}位为{1}'.format(lose, identity[lose - 1]))


if __name__ == "__main__":
    main()
# https://www.cnblogs.com/wunaozai/p/3933978.html
