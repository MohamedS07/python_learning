def timeConversion(s):
    for i in range(2):
        x=s[0]+s[1] 
    if s[8]+s[9]=='PM' and int(x)!=12:
        x=str(int(x)+12)
    if s[8]+s[9]=='AM' and int(x)==12:
        x='00'
    for i in range(2,8):
        x=x+s[i]
    print(x)
    
timeConversion('07:05:45PM')
    