responses=["Welcome to smart calculator", "My name is Cal",
           "Sorry this is beyond my ability"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def end():
    print(responses[2])
    input("Press enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[2])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"MINUS":sub,"SUBTRACTION":sub,
            "SUBTRACT":sub,"DIFFERENCE":sub,"PRODUCT":mul,"MULTIPLICATION":mul,"MULTIPLY":mul,
            "DIVIDE":div,"DIVISION":div,"LCM":lcm,"HCF":hcf,"+":add,"-":sub,"*":mul,"/":div}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}
            
