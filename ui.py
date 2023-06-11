import Note


def create_note():
    title = input('Enter note name: ')
    body = input('Enter note text: ')
    return Note.Note(title=title, body=body)


def menu():
    print("""Welcome to Notes program! 
    Implemented functions:
    1 - show all notes from file
    2 - add note
    3 - delete note
    4 - modify note
    5 - filter notes by date
    6 - show note by id
    7 - exit
    Please, enter function number: """)


def goodbuy():
    print("Program exited!")
