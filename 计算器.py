mode=int(input("请告诉我计算模式(1=区间加法,2=阶乘):"))
if mode==1:
    ans=0
    print("告诉我一个区间,我会计算出这里面所有整数的和")
    a=int(input("下限:"))
    b=int(input("上限:"))
    for c in range(a,b+1):
        ans=ans+c
    print("区间","(",a,",",b,")","的和为",ans)
if mode==2:
    ans=1
    a=int(input("给我一个数,我来计算它的阶乘:"))
    for c in range(1,a+1):
        ans=ans*c
    print(a,"的阶乘为:",ans)

