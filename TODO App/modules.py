import random
import json

def showNotes(notes):
    print("Your notes:")

    for i in notes.keys():
        name = notes[i]['name']
        text = f"| {notes[i]['text']}"
        textInArray = list(text)
        idd = f"ID: {i}"

        lent = len(text)
        c = 1

        k = 100
        while lent >= 100:
            textInArray[c*k] += " |\n\t\t| "

            lent -= 100
            c += 1
        
        text = ""
        for z in textInArray:
            text += z

        text += (101 - lent) * " " + "|"

        print(
            f'''
                 ---- {name} {'-' * (100 - len(name) - 5)}
                {text}
                 {'-' * (100 - len(idd) - 5)} {idd} ----
            '''
        )

    if not notes:
        print(
            '''
                 -------------------
                | There is no notes |
                 -------------------
            '''
        )

def nameAndTextChecker(name, text, notes, idd, Note):
    if (name == "" or name.isspace() or len(name) > 50) or (text == "" or text.isspace()):
        if (name == "" or name.isspace() or len(name) > 50) and (text == "" or text.isspace()):
            print("Invalid Name and Text")
        elif name == "" or name.isspace() or len(name) > 50:
            print("Invalid Name")
        else:
            print("Invalid Text")
    else:
        if Note == None:
            notes[idd]['name'] = name
            notes[idd]['text'] = text

            with open('notes.json', 'w') as file:
                json.dump(notes, file)

            print("Done :)")
        else:
            note = Note(name, text)
            notes[f'{note.generateId()}'] = {"name": note.getName(), "text": note.getText()}
            with open('notes.json', 'w') as file:
                json.dump(notes, file)

            print("Done :)")

def nameChecker(newName, notes, idd):
    if newName == "" or newName.isspace() or len(newName) > 50:
        print("Invalid Name")
    else:
        notes[idd]['name'] = newName

        with open('notes.json', 'w') as file:
            json.dump(notes, file)

        print("Done :)")

def textChecker(newText, notes, idd):
    if newText == "" or newText.isspace():
        print("Invalid Text")
    else:
        notes[idd]['text'] = newText

        with open('notes.json', 'w') as file:
            json.dump(notes, file)

        print("Done :)")

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
