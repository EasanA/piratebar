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

preferences = {}
#Ask customer what they like
def taste():
    print("Please answer Yes or No to the following: ")
    for question in questions:
        if input(questions.get(question)) in ['y', 'yes']:
            preferences[question] = True
        else:
            preferences[question] = False
#combine likes in random fashions    
def mix(preferences):
    print("Ye drink consists 'o: ")
    for ingredient in ingredients:
        if preferences[ingredient] == True:
            print(random.choice(ingredients.get(ingredient)))
        
if __name__ == '__main__':
    drinking = input("Ahoy, would ye like to wet ye tongue, bucko?")
    if drinking == "yes" or "y":
        taste()
        mix(preferences)
    else:
        print("Get out 'o me bar")