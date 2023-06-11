import file_operation
import Note
import ui


def add():
    note = ui.create_note()
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Note added successfully!')


def show(text):
    no_note = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Enter date, formatted by dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            no_note = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            no_note = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            no_note = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if no_note:
        print('No any notes!')


def id_edit_del_show(text):
    id = input('Enter note id: ')
    array = file_operation.read_file()
    no_note = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            no_note = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Note changed successfully!')
            if text == 'del':
                array.remove(notes)
                print('Note deleted successfully!')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if no_note:
        print('No note with entered id!')
    file_operation.write_file(array, 'a')
