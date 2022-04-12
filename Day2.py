from operator import truediv


print ("Day2 Starts")


#datatypes

#Day1 was about strings 

print ("Hello"[4]) #5th world will be printed 

# "123" is a considered as string when ypu are working with ""

print(123+365) # integer

#Float

exampleOfFloat =3141.59

#boolean

exampleOfBoolean = True

#underscore is used by the large numbers to make more readable format but act as an integer


#len() function does not work with integer function

# type() function checks the data type of a function 

print(type(exampleOfBoolean))

#converting variable into another data type

num_char = len(input("What is your name"))
new_num_char= str(num_char)
print("Your name has "+ new_num_char + "  characters. ")

 #Operators

print(3+5) #addition of two numbers
print(7-4) # Subtraction of two numbers
print(3*2) # Multiplication of two numbers
print(6/3) # Division of number gives float result
print(type(6/3))    
print(2**3) # to the power of , 2 to the power of 3
#PEMDAS () ** * / + -

print(int(6/3)) # this can be used when you just want the integer part
#in the above case everything that is mentioned after . is removed

print(round(8/3,2)) #round is self explainatory and the other parameter 2 is basically the precission upto this digit

# += , -=, 

score=0
score+=1
height=1.8
isWinning = True
#F-String 
print("your score is +")
print(f"yout score is {score}, your heigh is {height} and you are winning {isWinning}") 

