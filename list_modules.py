def make_intlist():#Makes a list of only integers out of the input_str
    print('Digit the integer elements of the list separated by commas("x,y,z"). Press "." when you are done: ')
    intlist=[]
    while True:
        input_str=input()
        if input_str==".":
            break
        c=input_str.split(",")
        for i in c:
            intlist.append(int(i))
    return intlist

#x=make_intlist()
#print(x)

def make_floatlist():#Makes a list of only floats out of the input_str
    print('Digit the float elements of the list separated by commas("x,y,z"). Press "." when you are done: ')
    floatlist=[]
    while True:
        input_str=input()
        if input_str==".":
            break
        c=input_str.split(",")
        for i in c:
            floatlist.append(float(i))
    return floatlist

#x=make_floatlist()
#print(x)

def search_for(floatlist, element):#Search for variable "element" in a given floatlist
    if element in floatlist:
        return True
    return False#If the element exists in the list, the fuction returns boolean "True"
                  #otherwise it returns "False"

#x=search_for([1,3,4,5,66],3)
#print(x)

#x=search_for(make_floatlist(),3) #note that "floatlist" could be = to "make_floatlist()"
#print(x)