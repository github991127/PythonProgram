import math
def funEquation(a,b,c):
    if(a==0):#一次方程
        if(b==0): return("error")
        else: return("x=%d"%(-c/b))
    else:
        d=b*b-4*a*c;
        if(math.fabs(d)<=1e-6):#即==0（double防止溢出）
            print("x1=x2=%d"%(-b/(2*a)))
        elif(d>1e-6):
            x1=(-b+math.sqrt(d))/(2*a)
            x2=(-b-math.sqrt(d))/(2*a)
            return("x1=%d,x2=%d"%(x1,x2))
        else: return("方程无实根")
if __name__ == "__main__":
    x=funEquation(1,5,6)
    #x=funEquation(0,1,5)
    #x=funEquation(0,0,5)
    print (x)
