# A='ismail'
# B="rami"
# S='''we have a computer,
# and it is a good thing
# ,and we are happy'''
# print(S)
# print(A)
# print(B)
# print(type(A))
# # string is An ary of characters  
# sttr="mohammed"
# print(sttr[0])
# print(sttr[3])
# print(sttr[5])
# # slicing {اقتطاع جزء من النص}
# print(sttr[0:5])
# print(sttr[5:8])
# print(sttr[:])
# print(sttr[-7:-1])
# print(sttr[-2:])
# print(sttr[-6:])
# # number of character
# print(len(A))
# print(len(sttr))
# string method -----------------------
# (1)strip()'remove the space  in begining or inding'
# STR="  hello  ,  word  "
# print(STR)
# print(STR.strip())
# print(STR.rstrip())
# print(STR.lstrip())
print('-----------')
# (2)upper ,lower
# print(STR.upper())
# print(STR.lower())
# print(STR.islower())
# print(STR.isupper())
# (3)replace
# print(STR.replace("h","m"))
# print(STR.replace("h",""))
# print(STR.replace("o","m"))
# print(STR.replace("s","m"))
# print(STR.replace("o","m",1))
# STR=STR.replace("h","m")
# print(STR) 
#  تعديل على القيمة بشكل كامل وداآم
# (4)split---------------تقسيم النص على حسب القيمة المعطاة والا يقسمها على المسافة الموجودة 
# print(STR.split("l"))
# print(STR.split())
# (5)center---------------------
# print(STR.center(20,"'"))
# print(STR.center(20,"*"))
# # (6) count عدد مرات تكرار الحرف 
# print(STR.count("l"))
# print(STR.count(""))
#    (7)(index)----------------رقم الحرف في النسص 
# print(STR.index("o"))
# print(STR.index("o",0,12))
# print(STR.index("o",0,20))
# print(STR.index("o",8,12))
# (8)find-------------------- ايجاد رقم الحرف في النص واذا لم يكن موجود يعود بقيمة -1 not Error
# print(STR.find("o"))
# print(STR.find("o",0,20))
# print(STR.find("o",8,13))
# check string ------------string in or not
# A="ismail junid"
# print("ail"in A)
# print("ail" not in A)
# format String  ------you cannot concatenate String with int
# name="Ali"
# Age=23
# greed=89.45694
# print( "my name is : "+name "and my Age is :"+Age) error
# print("my name is : {}".format(name))
# print("my name is : {},and my Age is {}".format(name,Age))
# print("my name is : {},and my Age is {} And my nationalety is {}".format(name,Age,"palistnian"))
# print("my greed is {:.5f}".format(greed))
# print("my name is : {},and my Age is {} And my nationalety is {} And my greed is {:.2f}".format(name,Age,"palistnian",greed))
# a,b,c ="one","tow","three"
# print("the number,{},{},{}".format(a,b,c))
# print("the number,{1},{2},{0}".format(a,b,c))
# print("the number,{1},{2},{3}".format(a,b,c))---------error
# format in varsion 3.3+
# print(f"my name is :{name} and my Age is:{Age} And my greed is :{greed}")
# ///user input____________++++++++++++_____
# name =input("inter your name")
# Age = input("inter your Age ")
# greed=input("inter your greed")
# print(f"your name is: '{name}'And my Age is :{Age} And my greed is :{greed}")
# number1=int(input("inter number1"))
# number2=int(input("inter number2"))
# number3=int(input("inter number3"))
# number4=int(input("inter number4"))
# # number5=float(input("inter number5"))
# sum=number1+number2+number3+number4
# print(f" the resalte is: {sum} ")
# print(type(sum))
# example(1)convert temprecher   F---->C
fahren=int(input("inter temp"))
cel=(fahren-32)*5/9
print(f"temp celsius={cel}")
