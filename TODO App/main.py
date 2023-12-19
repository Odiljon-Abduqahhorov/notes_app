from modules import Note, showNotes
import json

notes = {}
with open('notes.json') as file:
    try:
        notes = json.load(file)
    except:
        pass

print('\n')
print(" " * 25 + "<<< Todo App >>>")
print('\n')
print("Instructions: \n\t\tTo add note -> type '+' \n\t\tTo edit -> type 'e' \n\t\tTo remove a note -> type 'r' \n\t\tTo display your notes -> type 's'  \n\t\tTo exit program -> type 'cancel'")
print('\n')

showNotes(notes)

while True:
    val = input(">>> ")

    if val == "+":
        name = input("Name a note: ")
        text = input("Type a note: ")

        note = Note(name, text)
        notes[f'{note.generateId()}'] = {"name": note.getName(), "text": note.getText()}

        with open('notes.json', 'w') as file:
            json.dump(notes, file)

        print("Done :)")        
    elif val == "e":
        if not notes:
            print("Nothing to edit")
        else:
            idd = input("Please type an id of note you are going to edit, which is under the every note \n>>> ")
            getVal = notes.get(idd, "Invalid ID")
            if getVal == "Invalid ID":
                print(getVal)
            else:
                val = input("Which of these are you going to edit ? \nType n (name) / t (text) / b (both name and text) >>> ").lower()
                cname = notes[idd]['name']
                ctext = notes[idd]['text']

                if val == "n":
                    print('\n')
                    print(f"Current Name: {cname}")
                    newName = input("New Name >>> ")
                    notes[idd]['name'] = newName

                    with open('notes.json', 'w') as file:
                        json.dump(notes, file)

                    print("Done :)")
                elif val == "t":
                    print('\n')
                    print(f"Current Text: {ctext}")
                    newText = input("New Text >>> ")
                    notes[idd]['text'] = newText

                    with open('notes.json', 'w') as file:
                        json.dump(notes, file)

                    print("Done :)")
                else:
                    print('\n')
                    print(f"Current Name: {cname}")
                    newName = input("New Name >>> ")
                    print('\n')
                    print(f"Current Text: {ctext}")
                    newText = input("New Text >>> ")

                    notes[idd]['name'] = newName
                    notes[idd]['text'] = newText

                    with open('notes.json', 'w') as file:
                        json.dump(notes, file)

                    print("Done :)")
    elif val == 'r':
        if not notes:
            print("Nothing to remove")
        else:
            idd = input("Please type an id of note you are going to remove, which is under the every note \n>>> ")
            getVal = notes.get(idd, "Invalid ID")

            if getVal == "Invalid ID":
                print(getVal)
            else:
                notes.pop(idd)
                print("Done :)")

                with open('notes.json', 'w') as file:
                    json.dump(notes, file)
    elif val == 's':
        print('\n')
        showNotes(notes)
    elif val == 'cancel':
        exit(0)