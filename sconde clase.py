# numbers.........................
# complex number.....(real partr and imaginary part )
# mycmplex=5+6j
# print(type(my_complex))
# print("the real part is:{}".format(my_complex.real))
# print("the imaginary part is:{}".format(my_complex.imag))
# [1]you can convert from int to float or complex
# [2]# you can convert from float to int or complex   
# [3]you can not convert from complex to int or float
# N=100
# print(N)
# print(float(N))
# print(complex(N))
# A=25.2
# print(int(A))
# print(complex(A))
# operators of number............................................
# exponent   ................الأسس
# print(5**2)
# print(2**3)
# # floor devision...........................the int of the numbers.....
# print(100//5)
# print(110//5)
# print(119//20)
# print(120//7)
# print(139//7)
# the lists[] ..........................................
# my_list=[ 1,2,"one ","tow",100.5,True]
# print(my_list)
# print(my_list[0])
# print(my_list[5])
# print(my_list[4])
# print(my_list[2].upper())
# print(my_list[0]//5)
# print(my_list[1]/6)
# print(my_list[1:4])#slice
# print(my_list[::2])
# my_list[5]=3
# print(my_list)
# my_list[1:4]=["S","55","ismail",77,False,"ahmad",[5,6,8]]
# print(my_list)
# method of list...............................
#[1]append()..................add item
# A=["ahmed","yousuf","saaed"]
# A.append("ismail")
# A.append(5)
# print(A)
# B=["mohammed","rami",True,150.340]
# A.append(B)
# print(A)
# print(A[5])
# print(A[5][0])
# print(A[5][3])
# [2]extend()..........الاحتواء....
# AS=[1,2,3,4]
# VS=["one","tow","three","four"]
# CS=[True,False,10520.55]
# AS.extend(VS)
# print(AS)
# AS.extend(CS)
# print(AS)
# [3]remove()......................
# X=["ismail","salem","mosa","jake",108,70.55,True]
# X.remove("jake")
# print(X)
# [4]sort()............arrange the number in list...cannot use the string with number ..but you can use the string aloan.
# Y=[1,22,-15,55,104,-30,12]
# Y.sort()
# print(Y)
# Y.sort(reverse=True)#sort(reverse=false)....>>>normal arrange
# print(Y)
# C=["e","f","d","c","b","a"]
# C.sort()
# print(C)
# C.sort(reverse=True)
# print(C)
# [5] reverse()........reverse the item of list...............................................
# Z=[10,20,22,"hafiz",50,104,-30,-22,"ismail"]
# Z.reverse()
# print(Z)
# [6]clear()......remove the item of list 
# a=[1,2,3,10,40,401,"ismail"]
# a.clear()
# print(a)
# [7]copy()...........copy list
# b=[1,2,3,10,20]
# print(b)
# c=b.copy()
# print(c)
# b.append(5)
# print(b)#main list
# print(c)#copied list
# [8]count()................
# D=[1,20,55,22,6,9,22,"ismail","mma"]
# print(D.count(22))
# [9]index()..............to find the item.......
# E=["ismail","ramy","salem","mosa","ismail","ahmed","msaab","hafiz"]
# print(E.index("hafiz"))
# print(E.index("ismail"))
# [10]insert()........inter items before the item you sllected..........
# F=["ismail",102,-88,"tareq"]
# F.insert(0,"test")
# F.insert(-1,"mohammed")
# F.insert(1,True)
# print(F)
# [11]pop()..............................
# G=[1,5,44,28,"oop"]
# print(G.pop(-1))
# print(G.pop(2))
# print(G.pop(0))
# tuples)(iu,u,i,i,i,)...............................................
# my_tuple_one=("ismail","ramy",22)
# my_tuple_tow="ismail","fady",5,22.7,3,True
# print(my_tuple_one)
# print(my_tuple_tow)
# print(my_tuple_tow[0])
# print(my_tuple_tow[-1])
# print(my_tuple_tow[-3])
# print(my_tuple_tow[2])
# you cannot change the items of tuples
# operators used in string and list available in tuple 
# (1)tuple with one element  ("",) .........................
# my_tuple=("ismail",)
# print(type(my_tuple))
# my_tuple2="ismail",
# print(type(my_tuple2))
# print(len(my_tuple))
# print(len(my_tuple2))
# (2)tuple concatenation.................. 
# a=(1,2,3,101,4,5,5,8)
# b=(4,45,22,10,11,101,40)
# c=a+b
# print(c)
# d=a+b+("a","b","c",True)
# print(d)
# # (3) tuple string list repeat(*)..........
# my_tuple=("ismail",1,6)
# my_string="mohammed"
# my_list=["a","b","c"]
# print(my_tuple*5)
# print(my_list*5)
# print(my_string*5)
# methods ==>>{1} count.............
# A=(1,2,3,8,5,2,4,2,2,5,10,144,55)
# print(A.count(2))
# # {2}index().....................................
# B=(1,2,10,11,12,44,1542,2.22,1.33,True)
# print("the position of index is:{}".format(B.index(11)))
# print(f"the position of index is:{B.index(11)}")#format
#tuples destruct................................................. 
# S=("A","B",55,"C")
# x,y, _ ,z=S
# print(x)
# print(y)
# print(z)
# {...set}...............................................
# the set is not ordered and not indexed and not slicing....
# my_set={"ismail","Ahmed",104,11,"ali",True}
# print(my_set)
# print(my_set[0])error
# print(my_set[1:4])error
# you cannot use lest or dictionary inn set items
# my_set={"ismail","Ahmed",104,11,"ali",True,[5,"a"]}#unhashable type: 'list'
# my_set={"ismail","Ahmed",104,11,"ali",True,(5,"a")}
# print(my_set)
# set items is unique...................
# Ma_set={"ismail","mohammed","ismail",1,11,101,1,22,55,22}
# print(Ma_set)
# ()..set methods
# clear()...........................
# A={1,2,3,5,4,44,2,22,5}
# A.clear()
# print(A)
# union()....................
# B={"ismail","mohammed","basem","roba"}
# C={1,3,22,55,201.5}
# x={"A","b","c"}
# print(B.union(C))
# print(B|C)
# print(B.union(C,x))
# add()..................................
# S={1,2,3,101.55,44}
# S.add(88.2)
# # S.add(44.5,55)#error takes exactly one argument 
# print(S)
# copy().............................
# P={1,2,3,4,5,1014,65,7,6}
# f=P.copy()
# print(P)
# print(f)
# P.add(88.4)
# print(P)
# print(f)
# remove()............................
# D={1,5,55,40,42}
# D.remove(55)
# # D.remove(88.4)KeyError: 88.4
# print(D)
# discard().........................
# H={1,2,3,4,5,55,88.4}
# H.discard(55)
# # H.discard(10000)#no error 
# print(H)
# pop()..................
# L={1,2,3,4,5,55,88.4,True,"ismail","a",104.88}
# print(L.pop())#random element
# update()--------------------------------------
# J={1,2,3,4,5,6}
# K={"one","tow","three","four"}
# J.update(K)
# print(J)
# J.update([55,"b","A"])
# print(J)
# difference()-----------------------------------------------
# a={1,2,3,4,5}
# b={12,1,2,3,4,"one","tow",False}
# print(a)
# print(a.difference(b))
# print(a-b)
# print(b.difference(a))
# print(b-a)
# print("-"*40)
# # difference_update()-----------------------------------------------
# c={1,2,3,4,5}
# d={12,1,2,3,4,"one","tow",False}
# print(c)
# c.difference_update(d)
# print(c)
# d.difference_update(c)
# print(d)
# print("-"*40)
# intersection().................common element........................
# AS={1,2,3,"A","b",55.104}
# BS={"ismail","A","xyz",55.104}
# print(AS)
# print(AS.intersection(BS))
# print(AS)
# print("#"*50)
# # intersection_update()...................  .   ..  
# AS={1,2,3,"A","b",55.104}
# BS={"ismail","A","xyz",55.104}
# print(AS)
# AS.intersection_update(BS)
# print(AS)
# symmetric_difference()...........not common element.......................
# i={1,2,3,4,5,"x"}
# f={"hello","hi","A",1,2,3,"x"}
# print(i)
# print(i.symmetric_difference(f))#i^f
# print(i)
# print("%"*40)
# # symmetric_difference_update()
# i={1,2,3,4,5,"x"}
# f={"hello","hi","A",1,2,3,"x"}
# print(i)
# i.symmetric_difference_update(f)
# print(i)#i^f

# issuperset()...... .........................................................
# W={1,2,3,4}
# Z={1,2,3}
# C={1,2,3,4,5,6,7,8,9,10,11}
# print(W.issuperset(Z))#true
# print(Z.issuperset(W))#false
# print("%"*40)
# # issubset()............................
# print(W.issubset(C))#tru
# print(W.issubset(Z))#false
# print(Z.issubset(C))#tru
# print(Z.issubset(W))#true
# isdisjoint()................ are the sets without common items-------------------
g={1,2,3,4}
h={1,2,3}
r={44,2.5,84,9}
print(g.isdisjoint(h))
print(g.isdisjoint(r))
print(h.isdisjoint(g))
print(g.isdisjoint(g))
print(h.isdisjoint(r))






