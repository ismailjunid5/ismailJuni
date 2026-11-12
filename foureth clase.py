# control flow    ,,,,if ,,ifelse,,nested if
#   if condition
#   statement1
#   statement2
# else
# statement3
# statement4
# elif
#     statement5
#     statement6     
# U_name="ismail"
# U_country=input("inter your country")
# isStudent=input("are you student ?")
# C_name="python corse"
# C_prise=1000
# C_discount=0
# if U_country=="egypt"or U_country=="palestine":
#     C_discount=70
   
#     if isStudent=="yes":
#         C_discount=150
#         print(f"hi '{U_name}' because your from {U_country} and you are student")
#         print(f"the course '{C_name}' price is :{C_prise-C_discount}")
#     else:
#         print(f"hi '{U_name}' because your from {U_country}")
#         print(f"the course '{C_name}' price is :{C_prise-C_discount}")
# elif U_country=="ksa":
#     C_discount=50
#     print(f"hi '{U_name}' because your from {U_country}")
#     print(f"the course '{C_name}' price is :{C_prise-C_discount}")

# elif U_country=="kuwait":
#     C_discount=40
#     print(f"hi '{U_name}' because your from {U_country}")
#     print(f"the course '{C_name}' price is :{C_prise-C_discount}")
# else:
#        C_discount=0  
#        print(f"hi '{U_name}' because your from {U_country}")
#        print(f"the course '{C_name}' price is :{C_prise-C_discount}")

# ternary conditional operator.............................................
# country=input("inter your country")
# if country=="palestine":print(f"the weather in {country} us 15")
# elif country=="KSA":print(f"the weather in {country} us 31")
# else:print("country is not in the list")
    #  (short iF).................................................
# movie_Rate=18
# Age=21
# if Age<movie_Rate:
#     print("movie is not god for you")
# else:
#     print("movie is god for you and happy watching ")    
# print("movie is not god for you"if Age<movie_Rate else"movie is god for you and happy watching ")#short if 
# Age calculate (تمارين)...............................

# print("you can write the first letter or full name of the time unit".center(80,"_"))

# Age=int(input("please wright tour Age").strip())
# unit=input("please choice the time unite : month,weak,days.....").strip().lower()
# months=Age*12
# weeks=months*4
# days=Age*365
# hours=days*24
# minutes=hours*60
# if unit=="months"or unit=="m":
#         print(f"you lived for {months:,} month")
# elif unit=="weeks"or unit=="w":
#         print(f"you lived for {weeks:,} weeks")
# elif unit=="days"or unit=="d":
#           print(f"you lived for {days:,} days")
# elif unit=="hours"or unit=="h":
#           print(f"you lived for {hours:,} hours")
# elif unit=="minutes"or unit=="M":
#           print(f"you lived for {minutes:,} minutes")
# (in ,not in)................................................
# name="ismail"
# print("a"in name)
# print("l"in name)
# print("R"in name)
# print("v"in name)
# friend=["ismail","mohammed","rakan"]
# print("sayed"in friend)
# print("Ahmed"in friend)
# print("ismail"in friend)
# countries1=["egypt","palestine","qatar","KSA"]
# countries1_discount=80
# countries2=["italy","USA"]
# countries2_discount=50
# my_country="egypt"
# if my_country in countries1:
#     print(f"hello you have a discount equal to $ {countries1_discount}")
# elif my_country in countries2:
#         print(f"hello you have a discount equal to $ {countries2_discount}")
# else:
#       print("you have no discount")
# ........................................................................................
# admins=["Ahmed","Osman","Same","Ismail","Mohammed"] 
# name=input("please type your Name ").strip().capitalize()
# if name in admins:
#     print(f"hello {name} welcome bake")
#     option=input("delete or update your name ")
#     if option=='update':
#         new_name=input("your new name pleas").strip().capitalize()
#         admins[admins.index(name)]=new_name 
#         print("name updated")
#         print(new_name)
#     elif option=="delete":
#         admins.remove(name)
#         print("name deleted")
#         print(admins)
#     else:
#         print("wrong option selected")    
# else:
#     status=input ("you are not admen , Add you  yes  or no")     
#     if status=="yes"or status=="Y":
#         print("you have been Added")
#         admins.append(name)
#         print(admins)
#     else:
#         print("you ar not Added")    
# print("ismail")