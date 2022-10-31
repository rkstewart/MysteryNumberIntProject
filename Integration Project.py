#Name: Robert Stewart
#Program Description: Quiz Game

###############################################################################

print("Hello! Welcome to the magic quiz of Mystery!")
print("My name is Mr. Number, and today we will be finding:")
print('')
print("THE MAGIC NUMBER")
print("")
name = input("What is your name?")
print("Hello",name+", let's test your guessing skills.")
answer1 = input("what do you think the magic number is?")
#this will later be the correct answer despite math questions below
print("*buzzer* WRONG")
print("Given that you couldn't guess it first try, lets find out together!")
firstAnswer1 = int(input("What is a number between 29 and 86?"))
if ((firstAnswer1 <= 86) and (firstAnswer1 >= 29)):
    print("Great Job! You can do basic math!")
else: print("You somehow managed to get this question wrong, Try again")
secondAnswer2 = input("You passed the first question. Ready for more?")
if (secondAnswer2 == 'yes') or (secondAnswer2 == 'Yes') or (secondAnswer2 == 'yeah'):
    print("Great, let's continue", end='!') #couldn't find good use for
elif (secondAnswer2 == 'no' or secondAnswer2 == 'No' ):
    print("too bad " * 100)
else: print("Try again"),exit()
print('')
print("Lets say we have the "+"expression") #couldn't find use for 
print("x ** y == z % w")
print('')
print("We must set the expression to be true.")
print("The value of x and z is the answer you gave for 29<x<86")
print("Determine the value of y and w.")
yAnswer = input("What is the value of y for the expression to be true?")
wAnswer = input("What is the value of w for the expression to be true?")
#the 6 lines below are a cheat code to skip doing the math
#added for fun/to see if i could figure out the if statements
if (yAnswer == "idk"):
      continueNextQuestion = True
elif (wAnswer == "idk"):
      continueNextQuestion = True
elif int(firstAnswer1) ** float(yAnswer) == int(firstAnswer1) % float(wAnswer):
        continueNextQuestion = True
#plugs variables into expression and uses numerical operators
else: print("You got this question wrong, start over."),exit() 
if continueNextQuestion == True: 
      print("Great work! Now on to the next question")
print('')
print("Evalutate the expression below")
print("(w / /x * z) + (x - y / w)")
equationHalf=(float(wAnswer)//float(firstAnswer1)*float(firstAnswer1))
#Splitting the expression into two for character line limit
#the equation lines above and beneath plug in previous values to the expression
equationHalf2=(float(firstAnswer1)-float(yAnswer)/float(wAnswer))
#print(float(equationHalf)+float(equationHalf2))
finalAnswer = float(input("What is the value of the expression?"))
if finalAnswer == equationHalf + equationHalf2:
    print("Correct! You have found the magic number!")
else: print("Incorrect","Try again.", sep='. '), exit() #Couldn't find better use case
throwawayValue = input("Let's try one last time. What is the magic number?")
print("Wrong yet again")
print("The magic number is",format(float(answer1),"0.30f"))

   
