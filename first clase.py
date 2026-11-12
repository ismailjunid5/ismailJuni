# -----------------------
# type() show the data type
# all data in python is object
# ---------------------------
# print("ismail")
# print(10)
# print(type(10))  #integer
# print(type(100.2)) #float
# print(type("ismail"))  #string
# print(type([1,2,3,4,5]))    #f
# print (type((1,2,3,4))) #tuple
# print(type ({"one":1,"tow":2,"three":3}))#dectinary
# print(type(2==2)) #boolean
# # ------------------------------------------------------
# تسمية المتغيرات  A-Z,_,  you cannot use number spicial chr
# you can change the type of data before the rune
# لا يمكن استخدام كلمات النظام المحجوزة 
# number1=5
# print(number1)
# number2=15
# number3=2.5
# name="ismail"
# T=True
# number1="mohammad"
# print(number1)
#---------------    
# help("keywords")   # كل الكلمات المحجوزة في لغة بايثون 
# a,b,c,=1,2,3
# print(a,b,c)
# ------------------
# print("hello\b world")# bake space
# print("hello\
#     I love\
#     python") 
# print("ismail\\") #escape back slash
# print('i love single cot \' test\' \" ismail\"') #escape single and double quotes
# print("first line \n second line") #new line 
# print("1234567\rabc") #carriage return
# print("ismael\t junaid")#tab
# -----------------------------------
#  concatenate
# msg="hello"
# lang="world"
# print(msg+" "+lang)
# print(msg+"\n "+lang)
#### print(msg+" "+lang+5)  #thats error
# -----------------------------------
# string
# mas1="this is single cot 'test'"
# mas2='this is duble cot "tets"'
# print(mas1+" "+mas2)
# mas3="""first "test" 'test'
# second
# therd"""
# mas4='''a "test" 'test'
# d
# s
# f '''
# print(mas3+" "+mas4)
# ==============================
# the indexing (Access single item)
# mystring="I love python"
# print(mystring[0])# the first char from beginn
# print(mystring[-1])#first char from ind
# #slicing القطع اوالأجزاء
# print(mystring[5:9]) #begin......end of slice....the end is not includ...the spac is index..if start is not hear will start frome 0
# # if end is not hear will go to the end
# print(mystring[1:11])
# print(mystring[:10])
# print(mystring[3:])
# print(mystring[:])#full string
# # [beg:end:steps]
# print(mystring[0::1])#[beg0:end0:1]
# print(mystring[::2])#step 2 رح يفوت حرف يعني يكمشي حرف ويسيب التاني 
# print(mystring[::3])#step3رح يفوت حرفين
# ................string methods============
# str="my name is ismail"
# ste="        I love python     "
# print(len(str))#not method
# print(len(ste))#// // //
# #   strip///rsrip///lsrip
# # remove the character sellcted
# print(ste.strip())#remove the space 
# print(ste.rstrip())#strip for right
# print(ste.lstrip())#strip for left
# sto="##I love python###"
# print(sto.strip("#"))
# print(sto.rstrip("#"))#strip for right
# print(sto.lstrip("#"))#strip for left
# sto="@#$@I love python@#$@"
# print(sto.strip("@#$@"))
# print(sto.rstrip("@#$@"))#strip for right
# print(sto.lstrip("@#$@"))#strip for left
# title() method  first char in any word is capital...every char after the number is capital
# A="i love 3d graphic and 2d tochnology and Python"
# print(A.title())
# # capitalize() make   first char is capital 
# A="i love 3d graphic and 2d tochnology and Python"
# print(A.capitalize())
# # zfill............. عمل خانات تناسبب عدد الخانات المدخلة  
# c,d,e="1","11","121"
# print(c)
# print(d)
# print(e)
# print(c.zfill(3))
# print(d.zfill(3))
# print(e.zfill(3))
# upper().......................
# str="ismail"
# print(str.upper())
# # lower()............
# str="ISAMIL"
# print(str.lower())
# ...     split()...........return every element alon by space 
# a="i love python and php"
# print(a.split())
# a="ilovepythonandphp"
# print(a.split())#without space

# a="i#love#python#and#php"
# print(a.split("#"))#with index #
# a="i#love#python#and#php"
# print(a.split("#",2))#max split تأخذ أول عنصرين كل واحد على حدى أما الباقي لوحده عنصر واحد
# a="i#love#python#and#php"
# print(a.rsplit("#",2))#نفس الفكرة بس من اليمين
# center()...
# AS="isamil"
# print(AS.center(6))
# print(AS.center(8))
# print(AS.center(12,"#"))#hashing
# print(AS.center(15,"@"))# @
# count(كلمة كم مرةتكررت,begen,end)..........
# SQ="i love python and php becuase php is ease and simple and funny"
# print(SQ.count("and"))
# print(SQ.count("and",0,9))
# print(SQ.count("and",5,25))
# print(SQ.count("php",11))

# swapcase() chang any char from capital to small and small to capital
# F="I loVe PyTHon"
# G="I LOve pYthON"
# print(F.swapcase())
# print(G.swapcase())
# start_with()....هل يبدأ النص بهذا الحرف 
# I="I love python"
# print(I.startswith("I"))
# print(I.startswith("s"))
# print(I.startswith("v",4,9))

# # endwith() هل ينتهي النص بهذا الحرف 
# I="I love python"
# print(I.endswith("n"))
# print(I.endswith("s"))
# print(I.endswith("v",2,5))
# print(I.endswith("",2,7))
# index("sub of string ,biggen,end")).........
# A="i love python and my sql"
# print(A.index("p"))
# print(A.index("q",0,24))
# print(A.index("o",5,14))
# print(A.index("y",6))
# find("sub string ,start,end")......if the value is not fuond print -1
# A="i love python and my sql"
# print(A.find("p"))
# print(A.find("f",0,24))#is not fuond
# print(A.find("o",5,14))
# print(A.find("y",6))
# rjust(width,fill cha) ljust(width,fu=ill cha)............نفس عمل center
# R="ismail"
# print(R.rjust(17))
# print(R.rjust(17,"$"))
# print(R.rjust(17,"'"))
# print(R.ljust(17))
# print(R.ljust(17,"@"))
# print(R.ljust(17,"+"))
# splitline().............................
# P="""firts line
# sconde line 
# third line
# """
# print(P.splitlines()) 
# P="firts lin\nsconde line\n third line "
# print(P.splitlines())
# expandtabs()  control of tab........................
# v="hello \t i\tlove\tpython"
# print(v.expandtabs(15))
# one="I Love Python And 3G"
# print(one.istitle())
# tow="i Love Python And 3G"
# print(tow.istitle())
# four=""
# three=" "
# print(three.isspace())
# print(four.isspace())
# five="i love python"
# six="I Love python"
# print(five.islower())
# print(six.islower())
# seven="ismail_junid"
# eght="ismailjunid0100"
# nine="ismail#junid"
# print(seven.isidentifier())
# print(eght.isidentifier())
# print(nine.isidentifier())
# isalpha()....A-Z.............
# x="aaaasssdd"
# y="aaaasssss10"
# print(x.isalpha())
# print(y.isalpha())
# # isalnum()...A-Z and number
# xww="aaaasssdd"
# yww="aaaasssss10"
# print(xww.isalnum())
# print(yww.isalnum())
# replace(old value,new value,cunt)................
# ASD="hello one tow three one one "
# print(ASD.replace("one","1"))
# print(ASD.replace("one","1",1))
# print(ASD.replace("one","1",2))
# join(Iterable)............................
# mylist = ["ismail","abed" ,"junid"]
# print(" ".join(mylist))
# print("#".join(mylist))
# print("\t".join(mylist))
# print(" ,".join(mylist)
#  string format.................(old way).......................................................................
# name="ismail"
# Age=21
# ranke=10
# print("my name is "+name+"and my Age is "+Age +"my ranke is "+ranke) # error cnnt concatnat str and number
# print("my name is :%s"%(name))
# print("my name is :%s and my Age is %d and my ranke is :%f"%(name,Age,ranke))
# %s "string."...%d degeat ....%f floating 

# control floating point............
# mynumber=10
# print("my number is :%f"%mynumber)
# print("my number is :%.2f"%mynumber)
# print("my number is :%.0f"%mynumber)
# truncat string..................
# my_long_string ="hello my name is ismail whats your name and your email address"
# print("massage is :%s"%my_long_string)
# print("massage is :%.5s"%my_long_string)
# print("massage is :%.20s"%my_long_string)
#  string format.................(modern way).......................................................................
# name="ismail"
# number=593459101
# rank=102
# print("name is :{}".format(name))
# print("number is :{}".format(number))
# print("name is :{:s} and number is :{:d} and rank is :{:f} ".format(name ,number,rank))
# print("name is: {:s} and number is :{:d} and rank is :{:f} ".format(name ,number,rank))
# print("name is: {:s} and number is :{:d} and rank is :{:.2f} ".format(name ,number,rank))
# print("name is: {:s} and number is :{:d} and rank is :{:.0f} ".format(name ,number,rank))
# my_long_string ="hello my name is ismail whats your name and your email address"
# print("my long string ism :{:.12s}".format(my_long_string))
# print("my long string ism :{:.1s}".format(my_long_string))
# print("my long string ism :{:.7s}".format(my_long_string))
# format money...........................
# my_money=5951575421
# print("my money is :{:d}".format(my_money))
# print("my money is :{:_d}".format(my_money))
# print("my money is :{:,d}".format(my_money))
# rearrange items............................
# a,b,c="one","tow","three"
# print("hello{2}_{0}_{1}".format(a,b,c))
# print("hello{1}_{0}_{1}".format(a,b,c))
# print("hello:{0}_{0}_{1}".format(a,b,c))
# x,y,z=10,20,30
# print("the number is : {},{},{}".format(x,y,z))
# print("the number is : {2:d},{0:d},{1:d}".format(x,y,z))
# print("the number is : {2:f},{0:f},{1:f}".format(x,y,z))
# print("the number is : {0:.1f},{2:.3f},{1:.0f}".format(x,y,z))
# format in version 3.6+.......................................................
# name="ismail"
# Age=21
# print("my name is :{name}and my Age is:{Age}")
# print(f"my name is :{name}and my Age is:{Age}")

# ........................................................................................................








