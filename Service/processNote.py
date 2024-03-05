from datetime import datetime
from Exceptions.exception import IndexListException

from Model.listNotes import ListNotes
from Model.note import Note
from Service.validation import validation_note_number


def create_note() -> dict:
    ''' Создает запись '''
    title = input('Введите заголовок заметки: ')
    author = input('Введите автора: ')
    text = input('Введите текст заметки: ')
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_json = {
        'title': title,
        'author': author,
        'text': text,
        'data': data
    }
    return note_json


def edit_note(notes: ListNotes) -> None:
    ''' Редактирует запись '''
    try:
        note = get_note_by_number(notes)
    except Exception as e:
        if isinstance(e, ValueError):
            print(f'Неверный номер: {type(e).__name__} {e}')
        else:
            print('Невеный номер заметки')
        return
    data_note = create_note()
    print()
    setattr(note, 'title', data_note['title'])
    setattr(note, 'author', data_note['author'])
    setattr(note, 'text', data_note['text'])
    print('Изменения внесены')


def delete_note(notes: ListNotes) -> None:
    ''' Удаляет запись '''
    try:
        note = get_note_by_number(notes)
    except Exception as e:
        if isinstance(e, ValueError):
            print(f'Неверный номер: {type(e).__name__} {e}')
        else:
            print('Неверный номер заметки')
        return
    notes.get_notes().remove(note)
    print('Заметка удалена')


def get_note_by_number(notes: ListNotes) -> Note:
    ''' Возвращает номер заметки '''
    print('Введите номер заметки: ')
    notes.print_titles()
    note_number = int(input())
    if validation_note_number(notes, note_number):
        return notes.get_notes()[note_number]
