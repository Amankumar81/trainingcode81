# while loop
# i=6
# while(i<20):
#     print(i)
#     i+=1

# i=2
# while(i<10):
#     i+=1
#     if i==8:
#      continue
#     print(i)

# i=0
# while(i<10):
#    i+=1
#    if i==6:
#       break
#    print(i)

# i=1
# while(i<10):
#     print("aman upadhyay")
# else:
#     print("i is no longer")    

# function

# def my_function():
#    print("hello")
# for i in range(10):    
#  my_function()   #  function call

# i=0
# while(i<10):
#   print(i) 
#   i+=1
 

# def my_functio(name):
#     print(name+" "+"upadhyay")
# my_functio("aman")

# take user input function

# def my_functio(name):
#     print(name+" "+"sharma")  
# n=input("enter the name:")
# my_functio(n)

# # take user input in function multi time

# def my_functio(name):
#     print(name+" "+"sharma")
# for i in range(3):    
#  n=input("enter the name:")
#  my_functio(n)
  
# add 

# n1=int(input("enter the 1st  value"))
# n2=int(input(("enter the 2nd value")))
# result=n1+n2
# print(result)

# def my_function(name,age):
#     print(name,age)
# my_function("aman","20")

# take multi argument in function by use arg(*)

# def my_function(*kid):
#  print("the young is"+ kid[1])
# my_function("amna","mohit")
    
# pass multi aurg

# def my_function(*kid):
#  print("the young is"+ kid[1])
# my_function("amna","mohit")
    

 
# def my_function(counrty="india"):
#  print("i am from"+ counrty) 
# my_function()  
# my_function("india india")
  

# #square

# def square(n):
#   print(n*n)
# n=int(input("enter the value")) 
# square(n) 
  
# def square_element(input_lst)
#   tem=[]
#   for i in input_lst:
#     tem.append(i**2)
#   return tem  


# average by me

# def average(n):
#  print(avg/n)
# avg=0
# for i in range(10):
#  n=int(input("enter the value:"))
#  avg=n+avg
# average(n)  


# avg function by sir

# def avg_function(input_lst):
 
#     return(sum(input_lst)/len(input_lst))


# x=avg_function([23,24,26])
# print(x)

#  by predefine

# def mini(lst):
#  print(min(lst)) 
# mini([2,3,4,5,6]) 

# min by not predefine

# def mini(lst): # not 
#  minimun=x[0]
#  for i in lst:
#   if minimum>i:
#    minimum=i
#  return minimum  
# x=mini([2,3,4,5,6,7]) 
# print(x)

# lemda function pass take multi arg but expression single
# lambda arg : expression
# x= lambda a: a+10
# print(x(10))

# i=lambda a,b:a*b
# print(i(12,12))

# a=lambda y,b,c:y+b+c
# print(a(1,2,3))

#  pass lambda in function
# def my_func(n):
#     return lambda a:a*n
# double=my_func(2)
# print(double(22))


    #   pratice

# def lam(m):
#  return lambda a:a*m
# am=lam(2)
# print(am(5))

# def my_func(n):
#     return lambda a:a+n
# mn=my_func(5)
   
# calculator in python

# def add(n1,n2):
#     return n1+n2
# def sub(n1,n2):
#     return n1-n2 
# def mul(n1,n2):
#     return n1*n2
# def div(n1,n2):
#     return n1/n2

# n1=int(input("enter the value:"))
# ope=input("enter the operation:")
# n2=int(input("enter the value:"))
# if ope=='+':
#     add(n1,n2)
#     print(n1+n2)
# elif ope=='-':
#     sub(n1,n2)
#     print(n1-n2)
# elif ope=='*':
#     mul(n1,n2)
#     print(n1*n2) 
# elif ope=='/':
#     div(n1,n2)
#     print(n1/n2)
# else:
#     print("enter the rigit opeartor")           


class student:
    name="aman"
    rollno="23eldcs004"
    def __inti__(self):
        print("aman upadhyay")
s = student()    
print(s.name)

