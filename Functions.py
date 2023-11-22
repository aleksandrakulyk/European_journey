import random
def rand_choice(user_answer):
    results = []
    answers_1 = ['Water', 'Seafood', 'Hot', 'Apartment', 'Slow']
    answers_2 = ['Mountains', 'Pasta', 'Cold', 'Camping', 'Fast']
    options = {'warm_countries_water': ['Croatia', 'Cyprus', 'Greece', 'Malta', 'Portugal', 'Hungary'],
               'cold_countries_mountains': ['Austria', 'Chechia', 'Estonia', 'Romania', 'Slovakia', 'Poland',
                                            'Norwegian'],
               'warm_countries_mix': ['Bulgaria', 'France', 'Spain', 'Poland', 'Italy'],
               'cold_countries_city': ['Belgium', 'Denmark', 'Finland', 'Ireland', 'Lithuania', 'Luxemburg', 'Latvia',
                                       'Netherlands', 'Germany', 'Poland', 'Slovakia', 'Sweden']}
    if user_answer in answers_1:
        values = options.get('warm_countries_water')
        result = random.choice(values)
        results.append(result)
    elif user_answer in answers_2:
        values = options.get('cold_countries_mountains')
        result = random.choice(values)
        results.append(result)
    else:
        print('Wrong selection. Please make sure there is no typo.')
        user_answer = input("Water or mountains? ")
    return result

def Answers():
    answers = []
    answers_options = ['Water', 'Seafood', 'Hot', 'Apartment', 'Slow', 'Mountains', 'Pasta', 'Cold', 'Camping', 'Fast']
    questions = ["Water or Mountains?: ", "Seafood or Pasta? ", "Hot or Cold? ", "Camping or Apartment? ", "Fast or Slow "]
    for question in questions:
        user_answer = input(f"{question}").title()
        if user_answer not in answers_options:
           user_answer = input(f"Please make sure there is no typo. {question}").title()
        answers.append(user_answer)
    return answers