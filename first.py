# print('Hello World!')
# print('Hello World!\nWelcome') 

# name='Tim'
# print(name+'is a boy') #--> + need space
# print(name,'is 25 years old') # --> , no need space
# print(name)

# print(name.upper())
# print(name.isupper())

# print(len(name))
# print(name.index('T'))
# print(name.replace('m','ck'))

# number1 = 55
# number2 = str(number1)
# print("Number is ",number1)
# print("Number is ",number2)
# # print("Number is "+number1) ---> Error
# print("number is "+number2)

# print(abs(-5)) #output 5
# print(min(2,4,1,5))
# print(max(2,4,1,5))
# print(round(3.5))
# print(bin(3))
# print(bin(-3)) #binary

# from math import *
# print(sqrt(100))

# x= str(input("Enter Your Name "))
# y = int(input("Enter your Age "))
# print("Hi",x,"You are",y,"Years Old.")

sentence = str(input("Insert a sentence: "))
replace = str(input("Insert a word that you want replace: "))
replaced = str(input("Insert word what you want replace with: "))
print(sentence.replace(replace,replaced))
