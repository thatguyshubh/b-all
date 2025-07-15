import spacy
from ..keywords import slang, moves, bodyparts
nlp = spacy.load("en_core_web_sm")
initState = False
inputGiven = input("Send any request to continue:\n")
if not initState:
    initState = True
    print("Hey! Welcome to b(All)!")

doc = nlp(inputGiven)
print("\n Parsable tokens:")
for token in doc:
    if token.text.lower() in keywords.bodyparts:
        print("Found a match : ", {token.text}, "[BP]")