from Model.listNotes import ListNotes
from Service.utils import file_read, file_write, parse_json


def get_list_notes() -> ListNotes:
    ''' Получить список заметок '''
    filename = input('Введите имя файла: ')
    templates = file_read(filename)
    if templates is not None:
        return parse_json(templates)


def save_list_notes(list_notes: ListNotes):
    ''' Сохарнить список заметок '''
    filename = input('Введите имя файла: ')
    file_write(filename, list_notes)
