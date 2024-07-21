from datetime import date

def is_leapyear(y1):
    if(y1%4==0 and y1%100!=0 or y1%400==0):
        return True
    else:
        return False

def cal_leapyear(y1,y2):
    a=0;
    while(y1<y2):
        y1 += 1
        if(is_leapyear(y1)):a+=1
    return a

def is_rightdate(y,m,d):
    try:
        date(y, m, d)
    except:
        return False
    else:
        return True

def cal_month(y,m,d):
    if not is_rightdate(y,m,d):
        print("日期不合法")
        exit()
    count = 0  # count代表中间的闰年数
    month = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]  # 2021月份表
    dif = y - 2021
    if(dif>0):
        count=cal_leapyear(2021,y);
        if(is_leapyear(y)):
            i=2
            while(i<=11):
                month[i]+=1
                i+=1
        i=0
        while(i<=11):
            month[i]=(month[i]+dif+count)%7
            i += 1

    elif(dif<0):
        count=cal_leapyear(y,2021);
        if(is_leapyear(y)):
            i=0
            while(i<=1):
                month[i]-=1
                i += 1
        i=0
        while(i<=11):
            month[i]=(month[i]+2023+dif-count)%7;
            i += 1
    return month

def cal_week(month,m,d):
    return (month[m - 1] + d) % 7

def week(y,m,d):
    month = cal_month(y,m,d)
    out = cal_week(month, m, d)
    print(y,"年的月份表：")
    for i in month:
        print(i,end=' ')
    print("")
    return out

if __name__ == "__main__":
    #y = int(input("请输入年"))
    #m = int(input("请输入月"))
    #d = int(input("请输入日"))
    y=9999
    m=12
    d=31
    out = week(y,m,d)
    print("%d年%d月%d日是周%d" % (y, m, d, out))
