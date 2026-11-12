# Dictionary.............................................
# [1]dic items are contain key :value
#[2] dic key need to be immutable =>>(number,string,tuple) list not allowed
#[3]dic value can have any data type
#[4] dic key need to be unique
#[5]dik is not ordered you access its elements with key

# user={
# "name":"ismail",
# "Age":21,"country":"palestine",
# (1,2,3):"test",
# "skills":["python","html","mysql"],
# "rating":10.88
# }
# print(user)
# print(user["name"])
# print(user["Age"])
# print(user[(1,2,3)])
# print(user.get("skills"))
# print(user.keys())
# print(user.values())
# {{}} toe dimension dictionary.................................
# languages={
#     "one":{
#       "name":"html",
#     "progres":"50%"
#     },"tow":{
#     "name":"3g",
#     "progres":"90%"
#     }

# }
# print(languages)
# print(languages["one"])
# print(languages["one"]["name"])
# print(languages["tow"]["progres"])
# print(len(languages))
# print(len(languages["one"]))
# print(len(languages["tow"]))
# create dictionary from variables......................
# frame_work_one={"name":"ismail","Age":21,"rate":"90%"}
# frame_work_tow={"name":"mohammed","Age":25,"rate":"60%"}
# frame_work_three={"name":"rakan","Age":24,"rate":"80%"}

# all_frame_work={"one":frame_work_one,"tow":frame_work_tow,"three":frame_work_three}
# print(all_frame_work)
# print(all_frame_work["one"]["name"])
# print(all_frame_work["three"]["rate"])
# dictionary methods().........................................
# (1) clear()............................................
# user={"name":"ismail","age":21,"rate":"90%"}
# print(user.clear())
# (2)update()......................................
# user2={"name":"mohammed","Age":25,"rate":"60%"}
# user2["longe"]=185
# print(user2)
# user2.update({"wheat":"101"})
# print(user2)
# copy().........................
# user1={"name":"ismail","age":21,"rate":"90%"}
# b=user1.copy()
# print(b)
# user1.update({"wheat":"101"})
# print(user1)
# print(b)
# keys()values()...................
# print(user1.keys())
# print(user1.values())
# setdefault().................................
# user={"name":"ismail"}
# print(user)
# print(user.setdefault("name","Ahmed"))
# print(user)
# print(user.setdefault("Age",21))
# print(user)
# popitem()..........the last item you was index it .........................
# member={
# "name":"osama",
# "skill":"ps17"
# }
# print(member)
# member.update({"Age":27})
# print(member)
# print(member.popitem())
# items()..................................
# view={
# "name":"ismail",
# "skill":"Xbox360"
# }
# all_items=view.items()
# print(view)
# view["age"]=21
# print(all_items)
# fromkeys()..............................create a dic from tow tuples............
# a=("my_key_one","my_key_tow","my_key_three")
# b=("X","Y")
# print(dict.fromkeys(a,b))
# print(type(a))

# []boolean values******************************
# name=" "
# print(name.isspace())
# print(100>101)
# print(100>90)
# print(100>100)
# print(100>=100)
# print("-"*40)
# # True values..............
# print(bool("ismail"))
# print(bool(1000))
# print(bool(True))
# print(bool([1,2,3,45,7]))
# print("-"*40)
# # false values.................
# print(bool(0))
# print(bool(""))
# print(bool(''))
# print(bool([]))
# print(bool(False))
# print(bool({}))
# print(bool(()))
# print(bool(None))
# boolean operator......... {And ,or ,not}......................
# ..Assignment operator...{-=,+=,*=,/=,**=,%=,//=}...........................
# x=10 
# y=20
# # x=x+y
# x+=y
# print(x)
# x-=y
# print(x)
# x*=y
# print(x)
# x/=y
# print(x)
# x%=y
# print(x)
# x//=y
# print(x)
# comparison operator...........{<,>,==,<=,>=,!=}
# type conversion............................................
# str()...........
# a=10
# print(type(a))
# print(type(str(a)))
# # tuple()............
# c="ismail"  #string
# d=[1,2,3,4,5]#list
# e={"A","b","c"}#set
# f={"A":1,"b":2}#dictionary take the keys
# print(tuple(c))
# print(tuple(d))
# print(tuple(e))
# print(tuple(f))
# list()...................
# c="ismail"  #string
# d=(1,2,3,4,5)#tuple
# e={"A","b","c"}#set
# f={"A":1,"b":2}#dictionary take the keys
# print(list(c))
# print(list(d))
# print(list(e))
# print(list(f))
# print("+"*44)
# # set(............)
# c="ismail"  #string
# d=[1,2,3,4,5]#list
# e=("A","b","c")#tuple
f={"A":1,"b":2}#dictionary take the keys
# print(set(c))
# print(set(d))
# print(set(e))
# print(set(f))
# print("+"*44)
# dict()............................
# c="ismail"  #string you cannot convert
d=[["one",1],["tow",2],["three",3]]#list cane convert to duct by make nested list
e=(("A",1),("b",2),("c",3))#tuple you cane convert to duct by make nested tuple
# f={"A","b"}#set you cannot convert
# print(dict(c))
# print(dict(d))
# print(dict(e))
# print(dict(f))
# print("+"*44)
# print(str( type((e))))
# print(type (str(d)))
# print(type (str(f)))
# ************************************************
# user input[[[[]]]].......................
# f_name=input("what is your  first name ")
# l_name=input("what is your last name")
# number=input("inter your number")
# formate %%%%%%%%%%%%%%5
# f_name = f_name.strip().capitalize()
# l_name = l_name.strip().capitalize()
# print(f"hello {f_name.strip()} {l_name.strip()} nice to meat you And you number is {number.strip()}")
# print(f"hello {f_name} {l_name} nice to meat you And you number is {number}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++(email slice) تدريبات
# Name=input('what\'s your name ?').strip().capitalize()
# Email=input('what\'s your email ?').strip()
# User_name =Email[0:Email.index("@")]
# website=Email[Email.index("@")+1:]
# print(f"hello {Name} your Email is '{Email}'")
# print(f"your username is '{User_name}'\n and your website is '{website}' ")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++تدريبات==
# Age=int(input("what\'s your Age?").strip())
# print(Age)
# print(type(Age))
# months=Age*12
# weeks=months*4
# days=Age*365
# hours=days*24
# minutes=hours*60
# seconds=minutes*60
# print("you Lived for:")
# print(f"{months} months")
# print(f"{weeks:,} weeks")
# print(f"{days:,} days")
# print(f"{hours:,} hours")
# print(f"{minutes:,} minutes")
# print(f"{seconds:,} seconds")



