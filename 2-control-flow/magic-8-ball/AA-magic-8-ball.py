import random

#who will be asking the question
name = "Abena"

#what question is being asked
question = "Do you like mangoes"

#Space for answer
answer = ""

#generates random numbers to represent future answers
random_number = random.randint(1, 11)
# print(random_number)

#using conditional to assign different answers for each randomly generated value
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "Might be the case"
elif random_number == 11:
  answer = "No"
  #else statement for if the number was accidently assigned a value outside our range
else:
  answer = "Error"

#This is just in case there is no name present
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)
  
#This is if the user forgets to ask a question
if question == "":
  print("Error: Please enter question")
else:
  print("Magic 8-balls's answer: " + answer)