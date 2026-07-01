print ("Hello and welcome to my quiz about black holes! I hope you enjoy it and learn something new. Let's get started!")
start_code = input("Press enter or return to continue.")
print ("")
user_answer = input("Question 1: what color is a black hole?: ")
if user_answer == "black" or user_answer == "Black":
    print (user_answer)
    print ("Correct! Black holes are black.")
else:
    print ("Incorrect. The correct answer is black.")

user_answer = input("Question 2: what is the food related to black holes?: ")
if user_answer == "spaghetti" or user_answer == "Spaghetti":
    print (user_answer)
    print ("Correct! Spaghetti is related to black holes because of the term 'spaghettification'. ")
else:
    print ("Incorrect. The correct answer is spaghetti.")
    
user_answer = input("Question 3: are black holes real?: ")
if user_answer == "yes" or user_answer == "Yes":
    print (user_answer)
    print ("Correct! Black holes are real.")
else: 
    print ("Incorrect. The correct answer is yes.")