def calc(n1,n2):
    name = n1+n2
    true = "true"
    love = "love"
    num1 = 0
    num2 = 0
    for i in true:
        if i in name:
           num1+=1
    for i in love :
        if i in name:
            num2+=1
    num = (num1*10)+num2
    print(num)

calc("aksh","vart")
