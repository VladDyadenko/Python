# nam=input('Who are you?')
# print("Welkom", nam)

# inp=input("Europe floor?")
# usf=int(inp) +1
# print('US floor', usf)

# Пишемо коментар

# hours = 35
# pay = 2.75
# earn = hours * pay
# print("You earned", earn)

# Домашня робота 2.3

# hrs = input("Enter Hours:")
# print(hrs)
# hrs=float(hrs)
# rate= input("Enter Rate:")
# print(rate)
# rate=float(rate)
# pay=hrs*rate
# print("Pay:", pay)

# width = 17
# height = 12.0
# print(width//2)
# print(width/2.0)
# print(type(width))
# print(height/32)
# print(type(height))
# print(1+2*5)

# a=11
# if a<10 :
#     print("Less")
# if a> 10 :
#     print("More")

# x=10
# if x<2:
#     print("Little")
# elif x <10 :
#     print("Середній")
# else :
#     print("Big")
# print("successful")

# astr = "Hello Bob"
# try:
#     astr = int(astr)
# except:
#     astr = -1
# print("First", astr)

# astr = "25"
# try:
#     astr = int(astr)
# except:
#     astr = -1
# print("First", astr)

# Execise 3.1
# hrs = input("Enter Hours:")
# try:
#  h = float(hrs)   
# except:
#    print("Введіть число")
#    quit()
# rate = input("Enter Rate:")
# try:
#    rate= float(rate)   
# except:
#    print("Введіть число")
#    quit()
# rateUp = float(rate*1.5)
# if h<= 40 :
#     earn=h*rate
#     print(earn)
# else:
#     earn = (rate*40) + (h-40)*rateUp
#     print(earn)
# print(type(h))
# print(type(rate))
# print(type(rateUp))

# Execise 3.2
# score = input("Enter Score: ")
# try:
#   score = float(score)
# except:
#     print("Bad score")
#     quit()
# if score > 1.0:
#     print("Score mast be less 1.0")
#     quit()
# elif score >= 0.9 :
#     res ="A"
# elif score >=0.8 :
#     res ="B"
# elif score >= 0.7:
#     res="C"
# elif score >= 0.6:
#     res="D"
# elif score < 0.6:
#     res="F"
# print(res)


#Задача 4.1
# def computepay(h, r):
#     rateUp = float(r*1.5)
#     if h<= 40 :
#       earn=h*rate
#     else:
#       earn = (r*40) + (h-40)*rateUp
#     return print("Pay", earn)
 

# hrs = input("Enter Hours:")
# try:
#  h = float(hrs)   
# except:
#    print("Введіть число")
#    quit()
# rate = input("Enter Rate:")
# try:
#    rate= float(rate)   
# except:
#    print("Введіть число")
#    quit()
# p = computepay(h, rate)

# import random
# for i in range(10):
#     x = random.random()
#     print(x)
    

# while True:
#     line = input('>')
#     if line[0]== "#":
#         continue
#     if line == "done":
#         break
#     print(line)
# print("Done!")

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
     num=int(num)
    except:
       print("Invalid input")
       continue
    if smallest is None:
       smallest = num
    if smallest > num:
       smallest = num
    else :
       if largest is None:
          largest = num
       if largest < num:
         largest = num
print("Maximum is", largest)
print("Minimum is", smallest)