def fact_recur(x):#10,9,8,....1,0
    if x==0:#10!=0(f), 9!=0(f),8!=0(f),1!=0,0==0
        return 1
    else:
        return x*fact_recur(x-1)#10+sum(10-1),10+9+sum(9-1),10+9+8+sum(8-1)......
                        #10+9+8+7+6+5+4+3+2+sum(2-1)
                        #10+9+8+7+6+5+4+3+2+1+sum(1-1)
print("Fact:",fact_recur(70))