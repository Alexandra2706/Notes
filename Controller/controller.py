from Model.listNotes import ListNotes
from Model.note import Note
from Service.processNote import (create_note, delete_note, edit_note,
                                 search_by_date, search_by_id)
from Service.processList import get_list_notes, save_list_notes


def get_menu() -> None:
    end = False
    note = None
    notes = None
    while end == False:
        print(f'Выберите действие:\n'
              f'1 - открыть список заметок\n'
              f'2 - создать список заметок\n'
              f'3 - сохранить список заметок\n'
              f'4 - закрыть список заметок')
        if not isinstance(notes, type(None)):
            print(f'5 - добавить новую заметку\n'
                  f'6 - редактировать заметку\n'
                  f'7 - удалить заметку\n'
                  f'8 - найти заметку по дате\n'
                  f'9 - найти заметку по id\n'
                  f'10 - вывести список заметок')
        print(f'0 - выход\n')
        point = input()
        if point == '1':
            if not isinstance(notes, type(None)):
                print("Список заметок уже открыт")
            else:
                notes = get_list_notes()
            if not isinstance(notes, type(None)):
                print(notes)
        elif point == '2':
            if not isinstance(notes, type(None)):
                print(
                    f'Есть открытый список заметок.'
                    f'Перед созданием нового его надо закрыть')
            else:
                notes = ListNotes()
        elif point == '3':
            save_list_notes(notes)
        elif point == '4':
            answer = input('Вы уверены? [y/N]: ')
            if answer == 'y':
                notes = None
                print('Список заметок закрыт')
        elif point == '5':
            if isinstance(notes, type(None)):
                notes = ListNotes()
            data_note = create_note(notes)
            note = Note(data_note)
            notes.add_note(note)
        elif point == '6':
            if len(notes.get_notes()) == 0:
                print("Нет заметок для редактирования")
            else:
                edit_note(notes)
        elif point == '7':
            if len(notes.get_notes()) == 0:
                print("Нет заметок для удаления")
            else:
                delete_note(notes)
        elif point == '8':
            if len(notes.get_notes()) == 0:
                print("Нет заметок для поиска")
            else:
                search_by_date(notes)
        elif point == '9':
            if len(notes.get_notes()) == 0:
                print("Нет заметок для поиска")
            else:
                search_by_id(notes)
        elif point == '10':
            print(notes)
        elif point == '0':
            end = True
        else:
            print('Вы ввели неверное значение попробуйте еще раз')


def run():
    get_menu()
