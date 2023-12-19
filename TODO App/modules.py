import random

def showNotes(notes):
    print("Your notes:")
    for i in notes.keys():
        print(f"\t\t> {notes[i]['name']} : {notes[i]['text']}")
        print(f"\t\t{' ' * 20}ID:  {i}")
    if not notes:
        print(f"\t\tThere is no notes")
    print('\n')


class Note:
    def __init__(self, nname, ntext):
        self.__nname = nname
        self.__ntext = ntext

        self.__idIngredients = {
            'upper': list(range(65, 91)),
            "lower": list(range(97, 123)),
            "number": list(range(0, 10)),
            "sign": ['.', "?", "*"]
        }
    

    def generateId(self):
        ingred = self.__idIngredients

        upLett = random.choice(ingred['upper'])
        lowLett = random.choice(ingred['lower'])
        num = random.choice(ingred['number'])
        sign = random.choice(ingred['sign'])

        idPattern = f"#{num}{chr(upLett)}{sign}{chr(lowLett)}"

        return idPattern

    def getName(self):
        return self.__nname
    
    def getText(self):
        return self.__ntext