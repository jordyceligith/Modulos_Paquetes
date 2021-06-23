def F_to_K (f):

 ka=(f+459.67)*5/9

 return(ka)

def C_to_R (c):

 Ran=(c*9/5)+491.67

 return(Ran)
def C_to_F (c):

 far=(c*9/5)+32

 return(far)
def main():
    cont=0
    while cont<=100:
     print(cont,"C =",C_to_F(cont),"F")
     cont=cont+1
def con_C_R():
 cont=0
 while cont<=100:
     print(cont,"C =",C_to_R(cont),"R")
     cont=cont+1 
def con_f_K():
 cont=0
 while cont<=200:
     print(cont,"F =",F_to_K(cont),"k")
     cont=cont+1  
if __name__ == '__main__':
    main()
    con_f_K()
    con_C_R()
    