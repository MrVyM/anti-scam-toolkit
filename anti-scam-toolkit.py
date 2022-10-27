import random as rd 

def get_firstname(filename="names.txt") :
    lines = open(filename).read().splitlines()
    myline = rd.choice(lines)
    return myline


def __test() :
    print("firstname :",get_firstname())

if __name__=="__main__" :
    __test()
