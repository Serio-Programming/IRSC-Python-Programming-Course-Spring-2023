# Homework 2: Sentence Generator
# Program By: Tyler Serio
# File Name: H2_Sentence.py
# Function: This program will generate a random sentence

import random

articles = ("A", "THE", "THAT")
nouns = ("MAN", "WOMAN", "BOY", "GIRL", "CAT", "DOG", "BEAR", "DEER", "NEWT", "SALAMANDER")
verbs = ("HIT", "SAW", "BIT", "LIFTED", "DROP KICKED", "TALKED TO", "INVESTIGATED", "QUIETLY SHOUTED AT", "FIERCELY DEBATED FOURTEENTH CENTURY CHINESE POLITICS WITH", "CONSPIRED TO COMMIT MAIL FRAUD WITH")
prepositions  = ("BY", "WITH", "NEAR", "BEHIND", "NEXT TO", "ABOVE")

def generate():
    while True:
        nounPhrase = random.choice(articles) + " " + random.choice(nouns) + " "
        prepPhrase = random.choice(prepositions) + " " + random.choice(articles) + " " + random.choice(nouns) + " "
        verbPhrase = random.choice(verbs) + " " + random.choice(articles) + " " + random.choice(nouns) + " " + prepPhrase + " "
        sentence = nounPhrase + verbPhrase
        print(sentence)
        print("")
        print("Would you like to generate another sentence?")
        print("[any key] - yes")
        print("[n] - no")
        if input() == "n":
            exit()
        print("")

generate()


