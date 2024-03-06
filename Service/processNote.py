from datetime import datetime

from Model.listNotes import ListNotes
from Model.note import Note
from Service.validation import validation_data, validation_note_number


def create_note(notes: ListNotes) -> dict:
    ''' Создает запись '''
    id = set_id(notes)
    title = input('Введите заголовок заметки: ')
    text = input('Введите текст заметки: ')
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note_json = {
        'id': id,
        'title': title,
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
            print('Неверный номер заметки')
        return
    data_note = create_note(notes)
    print()
    setattr(note, 'title', data_note['title'])
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
    ''' Возвращает заметку по id '''
    print('Введите номер заметки: ')
    notes.print_titles()
    note_number = int(input())
    if validation_note_number(notes, note_number):
        return notes.get_notes()[note_number]


def set_id(notes: ListNotes) -> int:
    ''' Установить id для заметки'''
    if len(notes.get_notes()) == 0:
        return 0
    last_note = notes.get_notes()[-1]
    return getattr(last_note, 'id') + 1


def search_by_date(notes: ListNotes) -> None:
    result = []
    print('Введите дату в формате dd.mm.yyyy:')
    note_date = input()
    if validation_data(note_date):
        for obj in notes.get_notes():
            current_date = f'{getattr(obj, "data")[8:10]}.{getattr(obj, "data")[5:7]}.{getattr(obj, "data")[:4]}'
            if current_date == note_date:
                result.append(obj)
        if len(result) == 0:
            print('Заметки не найдены')
        else:
            print(*result)
    else:
        print('Дата невалидна')


def search_by_id(notes: ListNotes) -> None:
    ''' Поиск заметки по id '''
    try:
        result = get_note_by_number(notes)
        if isinstance(result, type(None)):
            print('Заметки не найдены')
        else:
            print(result)
    except Exception as e:
        if isinstance(e, ValueError):
            print(f'Неверный номер: {type(e).__name__} {e}')
        else:
            print('Неверный номер заметки')
        return
