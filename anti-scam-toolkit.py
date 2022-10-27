import random as rd 

def get_firstname(filename="names.txt") :
    lines = open(filename).read().splitlines()
    myline = rd.choice(lines)
    return myline

def get_extension(filename="extension.txt") :
    lines = open(filename).read().splitlines()
    myline = rd.choice(lines)
    return myline

def generate_email(firstname=get_firstname(),lastname=get_firstname(),extension=get_extension()) :
    return firstname+"."+lastname+"@"+extension

def generate_number(country="") :
    result = country
    if country == "" :
        result = "0"
    for i in range(9) :
        result+= str(rd.randint(0,9))
    return result

def __test() :
    print("firstname :",get_firstname())
    print("email :",generate_email())
    for i in range(4) :
        print("number :",generate_number())
    print("number :", generate_number("+33"))

if __name__=="__main__" :
    __test()
