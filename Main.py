
import random
import requests
import selectorlib
import pandas as pd
import Questionnaire as Quest

df = pd.read_csv("countries.csv")


class Questionnaire:
    def __init__(self, questions, answers_options, options):
        self.answers = []
        self.questions = questions
        self.answers_options = answers_options
        self.options = options

    def ask(self):
        for question in self.questions:
            user_answer = input(f"{question}").title()
            if user_answer not in self.answers_options:
                user_answer = input(f"Please make sure there is no typo. {question}").title()
            self.answers.append(user_answer)
        return self.answers

    @staticmethod
    def eliminate(results, country):
        filtered_results = [result for result in results if result != country]
        return filtered_results

    def rand_choice(self):
        results = []
        answers_1 = ['Water', 'Seafood', 'Hot', 'Apartment', 'Slow']
        for answer in answers:
            if answer in answers_1:
                values = self.options.get('warm_countries_water')
                if values:  # Ensure values is not None or empty
                    while True:
                        result = random.choice(values)
                        if result not in results:
                            results.append(result)
                            break
            else:
                values = self.options.get('cold_countries_mountains')
                if values:  # Ensure values is not None or empty
                    while True:
                        result = random.choice(values)
                        if result not in results:
                            results.append(result)
                            break
        return results


class WebScraper:
    def __init__(self):
        self.url = URL
        self.user_agent = user_agent

    def scrap(self):
        response = requests.get(URL, user_agent)
        source = response.text
        return source

    def extract(self, data_source):
        extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
        value = extractor.extract(data_source)
        value = str(value)[17:19]
        return value


# Starting the game
user_name = input("Hi! What is your name? ").title().strip()
print(f"Hello {user_name}! You do not know where to go this time? Let's play a game and decide together!")

# Asking the questions, answers collection and randomization
game = Questionnaire(Quest.QUESTIONS, Quest.ANSWERS_OPTIONS, Quest.OPTIONS)
answers = game.ask()
destinations = game.rand_choice()

#Eliminating country based on user preferences
user_input = (input("Is there any country you have visited lately and you don't want to got there this time? Yes/No: ")).title().strip()
if user_input == "Yes":
    user_country = input("Please type name of this country: ").title().strip()
    destinations = Questionnaire.eliminate(destinations, user_country)

#Printing destinations
print(f"Here you go! We advise you to go to: ")
destinations = [(index + 1, destination) for index, destination in enumerate(destinations)]

for index, destination in destinations:
    capital = df.loc[df["Country"] == destination, "Capital"].squeeze()
    URL = f"https://www.timeanddate.com/weather/{destination}/{capital}"
    user_agent = "user_agent"
    decision = WebScraper()
    temperatures = decision.scrap()
    temperature = decision.extract(temperatures)
    print(f"{index}. {destination} -- > Today's temperature in {capital}: {temperature} °C")






