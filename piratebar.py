#Ask Question, if true, choose random ingred., combine random ingred, give name, loop

#Create the random ingredients from the choices
import random

#Givens
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

yes = set(['yes','y', 'ye', ''])
no = set(['no','n'])


#Ask customer what they like
def taste():
    preferences = {}
    for type, question in questions.items():
        preferences[type]= input(question)
#combine likes in random fashions    
def mix(preferences):

if __name__ == '__main__':
drinking = input("Ahoy, would ye like to wet ye tongue, bucko?")
    if drinking == "y":
        taste()
        mix(preferences)
    else:
        print("Get out 'o me bar")
    