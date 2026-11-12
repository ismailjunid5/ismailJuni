# [A]choose the correct Answer  :---------------------
# 1.b, 2.d, 3.c, 4.d ,5.b ,6.d ,7.c ;
# [B]what the output of the cod :------------------
# {1}num1= 19 num 2= 7
# {2} {1
# ,0
# ,12}
# [C] solve the following question:--------------------------------- 
# Q1.#############
N1=int(input("inter the first number"))
N2=int(input("inter the seconde number"))
N3=int(input("inter the third number"))
if  N1>N2 and N1>N3 :
    print(f"{N1}:is the greatest number")
elif N2>N1 and N2>N3:
     print(f"{N2}:is the greatest number")   
elif N3>N1 and N3>N2:
     print(f"{N3}:is the greatest number")  
else:
    print("its not fund a greatest number ")
# Q2.###################
print("1.calculate cub volume \n2.calculate cylinder volume \n3. calculate cone volume")
choice=float(input("inter your choice "))

if choice==1:
    side=float(input("inter cub side"))
    cubVolume=side**3
    print(f"cub volume:{cubVolume}")
elif choice==2:
    radius=float(input("inter cylinder radius"))   
    hight=float(input("inter cylinder hight"))   
    cylinderVolume=hight*(3.14*radius**2)
    print(f"cylinderVolume : {cylinderVolume}")
elif choice==3:
    radius=float(input("inter cone radius"))   
    hight=float(input("inter cone hight")) 
    coneVolume=1/3*(hight*(3.14*radius**2))
    print(f"coneVolume : {coneVolume}")
elif choice==4:
    exit(0) 
else :
    print("not fund")   
# Q3.##############################
length=float(input("inter read length "))

if length==60:
    width=4
elif length>60 and length<=80:
    width=6
elif length>80:
    width=8
else:
    print("not available value")   
    exit(0) 
streetArea=length*width
# print(f"street Area : {streetArea}")
print(f"street length : {length}, street width: {width}, street area : {streetArea}  ")


