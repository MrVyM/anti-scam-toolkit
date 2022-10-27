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

def __test() :
    print("firstname :",get_firstname())
    print("email :",generate_email())

if __name__=="__main__" :
    __test()
