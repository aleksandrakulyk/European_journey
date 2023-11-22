import Functions as fc
import random

print("Hello! You do not know where to go this time? Let's play a game and decide together!")

# Elimination of visited countries

user_input = (input("Is there any country you have visited lately? Yes/No: ")).title()
user_input.strip()

if user_input not in ['Yes', 'No']:
    print("Word can't be recognized. Please try again!")
    user_input = (input("Is there any country you have visited lately? Yes/No: ")).title()

country = ""

#Selection of travel options depending on the user's response

if user_input == 'Yes':
    user_input_1 = input("Please type the name of this country: ")
    user_input_1.strip()
    country = user_input_1
    print("Please answer below 5 questions. Do not think to much, just choose your first association.")
else:
    print("So there is a lot to choose! Please answer below 5 questions. Do not think to much,"
          " just choose your first association.")

results = []
answers = fc.Answers()

for answer in answers:
    result = fc.rand_choice(answer)
    results.append(result)

output = set(results)

#Presentation of the randomly selected places:

for index, result in enumerate(output):
    if result == country:
        results.remove(country)
    number = index + 1
    print(number, '-', result)

user_action = input("Are you still not sure what to choose? Type yes or no ")

#Final draw

if user_action == 'yes':
    output = random.choice(results)
    print(f'This time we advise you to go to {output}. Happy journey!')
else:
    print("Happy journey then!")

#The End

