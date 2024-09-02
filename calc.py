def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

dict = {"+":add,"-":sub,"*":mult,"/":div}

def cacl():
    number1 = int(input("Enter the first number: "))
    accumulate = True


    while accumulate :
        operator = input("Enter an operator (+,-,*,/): ")
        number2 = int(input("Enter the second number: "))
        value = (dict[operator](number1,number2))
        print("Output value: ",value)

        cont = input("Want to continue calculation(Y/N): ").upper()
        if cont == 'Y':
            number1 = value
        else:
            accumulate = False
            print("New Calculaton: ")
            cacl()
